import pandas as pd
import numpy as np
import os
import sqlite3


def get_path(filename: str, search_dirs=['.', 'datasets']):
    '''Get the full path of the file

    Parameters
    ----------
    filename : str
        Name of the file to be searched
    search_dirs : list of str, optional
        List of subfolders to be searched. The default is ['.', 'datasets'].

    Returns
    -------
    path : str
        Full path of the file if found, and None otherwise
    '''
    working_directory = os.getcwd()

    found = False
    for subfolder in search_dirs:
        path = os.path.join(working_directory, subfolder, filename)
        path = os.path.abspath(path)
        if os.path.exists(path):
            return path
    return None


def init_db(db="overtime.db", emp_csv="employees.csv"):
    '''Initialize database and load employees info into employees table  

    Parameters
    ----------
    csv : str, optional
        Name of the CSV file to be read. The default is "employees.csv".
    db : str, optional
        Name of the DB to be created. The default is "overtime.db".

    Returns
    -------
    df : pandas dataframe
        Dataframe with the imported records

    '''
    csv = get_path(emp_csv)

    if csv is None:
        return None

    df = pd.read_csv(csv, parse_dates=['Onboard Date'])

    # transform Status from categorical data to numerical data
    df['Status'] = [1 if x == 'Active' else 0 for x in df['Status']]

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS employees")
    cursor.execute("DROP TABLE IF EXISTS requests")

    res = df.to_sql("employees", conn, index=False)

    # create requests data table if it doesn't exist in the db
    sql = "CREATE TABLE IF NOT EXISTS requests (\
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            Status TEXT NOT NULL, \
            [Start Date] TEXT, \
            [Full Name] TEXT NOT NULL, \
            Description TEXT, \
            Multiplier REAL, \
            Pager INTEGER, \
            [Primary] INTEGER, \
            [Pay Month] TEXT)"

    cursor.execute(sql)
    if res > 0:
        conn.commit()
        print("Data inserted successfully")
    else:
        print("Error in insertion")
    conn.close()


def add_records_from(csvfile, paymonth=None, db="overtime.db"):
    '''Add new overtime or pager requests to db, and create table if not exists

    Parameters
    ----------
    csv_file : str
        Name of the CSV file to be read.
    db: str, optional
        Name of the DB to be created. The default is "overtime.db".

    Returns
    -------
    filtered_df : pandas dataframe
        Dataframe with only approved requests
    '''
    csv = get_path(csvfile)

    if paymonth is None:
        paymonth = csvfile.split(".")[0].split("_")[1]
        paymonth = paymonth[:4] + "-" + paymonth[-2:]

    df = pd.read_csv(csv, parse_dates=['Start Date'])

    df.rename(columns={'Comp Ratio': 'Multiplier',
                       'Employee Name': 'Full Name'}, inplace=True)

    # convert Pager, Primary to 1, 0
    df['Pager'] = df['Description'].apply(
        lambda x: 1 if x.startswith('Pager') else 0)
    df['Primary'] = [1 if x == 'Primary' else 0 for x in df['Pager Role']]

    # Multiplier of pager requests is always 100% and should be converted to float
    df['Multiplier'] = [r['Multiplier'] if r['Pager'] == 0 else '100%'
                        for _, r in df[['Multiplier', 'Pager']].iterrows()]
    df['Multiplier'] = df['Multiplier'].apply(
        lambda x: float(x.strip('%'))/100)

    df.drop(columns=['Pager Role'], inplace=True)

    df['Start Date'] = df['Start Date'].dt.strftime('%Y-%m-%d')

    # add pay month
    df['Pay Month'] = paymonth

    # filter out other requests than Approved
    filtered_df = df.query("Status == 'Approved'")

    # add to database
    conn = sqlite3.connect(db)

    res = filtered_df.to_sql('requests', conn, if_exists='append', index=False)

    if res > 0:
        conn.commit()
        print(f"Added {res} rows to database")
    else:
        print("No rows added")
    conn.close()

    return filtered_df


def query(paymonth: str):
    '''Query the database for overtime and pager requests for a given month

    Parameters
    ----------
    paymonth : str
        Pay Month in the format of YYYY-MM

    Returns
    -------
    output : str
        Text output of the query results
    '''
    conn = sqlite3.connect("overtime.db")
    cursor = conn.cursor()

    sql = '''SELECT [Pay Month], [Start Date], employees.Emp_ID, requests.[Full Name],
                    Multiplier, Pager, employees.[Daily Wage] 
                FROM requests 
                LEFT JOIN employees ON requests.[Full Name] = employees.[Full Name] 
                WHERE [Pay Month] = ?'''

    records = cursor.execute(sql, (paymonth,)).fetchall()
    conn.close()

    paytable_cols = ['Pay Month', 'Start Date', 'Employee ID',
                     'Employee Name', 'Multiplier', 'Pager', 'Daily Rate']

    df = pd.DataFrame(records, columns=paytable_cols)

    if len(df) == 0:
        return "No query results found.\n"

    # adjust daily rate for pager requests
    df['Daily Rate'] = [rate if pager == 0 else 1000 for rate,
                        pager in zip(df['Daily Rate'], df['Pager'])]
    df['Start Date'] = pd.to_datetime(df['Start Date']).dt.strftime('%m/%d')

    # calculate the actual amount of each request
    df['Amount'] = df['Daily Rate'] * df['Multiplier']

    summary = df.groupby(by='Employee Name').agg(
        {'Employee ID': 'count', 'Amount': 'sum'}).reset_index()
    summary.columns = ['Employee', '# of Records', 'Total Amount']

    raw_text = df.to_string(index=False, justify="left")
    summary_text = summary.to_string(index=False, justify="left")

    output = f'''\n\nQuery Pay Month: {paymonth}
        \n\n>>>> Track records of Overtime and Pager requests:
        \n{raw_text}
        \n\n>>>> Amount Summary by employee:
        \n{summary_text}\n\n
        '''
    return output


if __name__ == '__main__':
    # init()
    # add_records_from("new_requests.csv", "2023-07")

    query("2023-06")
