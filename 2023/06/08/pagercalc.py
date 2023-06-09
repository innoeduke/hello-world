import pandas as pd
import numpy as np

DATA_DIR = './datasets/'


def read_employee_info(csvfile="employee_info.csv"):
    # specify dtype of all columns except for dates
    dtypes = {
        'employee_id': int,
        'employee_name': str,
        'employment_status': str,
        'job_title': str,
        'annual_base': float,
        'day_rate': float
    }

    # use parse_dates attribute to specify columns in date format
    path = DATA_DIR + csvfile
    df = pd.read_csv(path, dtype=dtypes, parse_dates=['date_onboard'])

    return df


def get_approved_records(csvfile="OT Compensation.csv"):
    dtypes = {
        'Status': str,
        'EmpName': str,
        'Description': str,
        'Role': str
    }

    path = DATA_DIR + csvfile
    df = pd.read_csv(path, parse_dates=['Start Date'], dtype=dtypes)

    df.rename(columns={"Employee Name": "employee_name",
                       "Comp Ratio": "multiplier",
                       "Status": "status",
                       "Description": "description",
                       "Start Date": "date_start",
                       "Pager Role": "pager_role"}, inplace=True)
    df['multiplier'] = df['multiplier'].str.rstrip('%').astype(float)/100

    return df.query("status == 'Approved'")


def load_new():
    # define the columns to be returned
    returned_columns = ['employee_id', 'employee_name', 'date_start',
                        'pager?', 'holiday_name', 'day_rate', 'multiplier', 'amount']

    # call the two methods above and merge employee info with overtime records
    df = pd.merge(left=get_approved_records(),
                  right=read_employee_info(), on='employee_name', how='left')

    # add a Pager? column: 1 for Pager and 0 for Holiday
    col_pager = pd.Series(index=df.index, dtype=int)

    # add Holiday column in str format to show the name of the holiday
    col_holiday = pd.Series(index=df.index, dtype=str)

    # extract pager? flag and holiday name from Description
    for index, row in df.iterrows():
        if row['description'].startswith("Holiday"):
            col_pager[index] = 0
            col_holiday[index] = row['description'].split("-")[1].strip()
        else:
            col_pager[index] = 1
            # adjust the daily rate of pager to 1000 RMB per week (2 days)
            df.loc[index, 'day_rate'] = 1000
            df.loc[index, 'multiplier'] = 1.0

    df['pager?'] = col_pager.astype(int)
    df['holiday_name'] = col_holiday.astype(str)

    # calculate the amount of a record
    df['amount'] = df['day_rate'] * df['multiplier']

    return df[returned_columns]


if __name__ == '__main__':

    print("\n\n>>>> Overtime and Pager Records this month:\n")

    df_new = load_new()
    print(df_new.to_string(index=False))

    print("\n\n>>>> Total overtime and pager records by employee:\n")

    result = df_new.groupby(by='employee_name').agg(
        {'employee_id': 'count', 'amount': 'sum'}).reset_index()
    result.columns = ['Employee', '# of Records', 'Total Amount']
    print(result.to_string(index=False))
