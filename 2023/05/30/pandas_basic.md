## Pandas Basics

Today I am going to start learning the basics of Pandas.

Pandas is a useful library for manipulating data.

We live in a big data world and data is everywhere in various forms. People have been well trained to use Excel to store data and create data charts. Think about this... why Excel could becomed popular, I would argue that a key reason is its tabular form of data representation. Let's understand this via an example.

**Example Case**

Suppose we have a group of students. Each student is a single person with different traits. To name a couple of examples: Sky is a boy from Grade 2 Class 4. His favorite sport is floor ball. Instead, Zelda is a girl from Grade 7 Class 3. Her favorite sport is boxing. It won't take many efforts to find out both students have a common set of traits: Name, Gendar, Grade, Class, Favorite Sport. The differences lie in the values of the traits. We can use a table to show such data:

| Name  | Gendar | Grade | Class | Favorite_Sport |
| ----- | ------ | ----- | ----- | -------------- |
| Sky   | Male   | G2    | C4    | Floorball      |
| Zelda | Female | G7    | C3    | Boxing         |

Pandas is extremely efficient and useful for managing such tabular data. It reads data into so called dataframes, and then provides a whole bunch of methods for manipulating the data.

1. First, we need to import Pandas.

   ```python
   import pandas as pd
   ```

2. Then we can create a dataframe.

   ```python
   df = pd.DataFrame(data = {
        'Name': ['Sky', 'Zelda'],
        'Gendar': ['Male', 'Female'],
        'Grade':['G2', 'G7'],
        'Class': ['C4', 'C3'],
        'Favorite_Sport': ['Floorball', 'Boxing']
    })
   ```

### Getting Started

Pandas use Series to hold a data vector and DataFrame to hold a data matrix. I'll start with four basic data operations: Create, Retrieve, Update and Delete, a.k.a. CRUD.

**Summary**

1. CREATE
   - Pandas use either DataFrame constructor, .from_somedatatype() functions \*or a bunch of read_somefiletype() functions to load data into DataFrame
2. RETRIEVE - column/row/cell
   - use `df[ col_name | col_list ]` to retrieve one or more columns
   - use `df.loc[ row_index | row_list ]` to retrieve one or more rows
   - use `df.iloc[ row_id, col_id ]` to retrieve a cell by numerical ids
3. UPDATE
   - assign values to retrieved cells or regions
   - use `apply()` method to update a vector
4. DELETE
   - use `drop(index, axis=[0|1], inplace=True)` to drop a row or column
   - use `dropna(inplace=True)` to drop all null values
   - use `<del df>` to delete a dataframe

When we get a dataset, the first thing we would do is to understand its data. Here're a few tasks to complete:

**Load the data**

- read/load data into a dataframe: `read\*(), from_dict()`
- get the shape of the dataframe: `.shape`
- get the data types of the columns: `.dtypes`
- get the column names: `.columns`

**Explore data to get some senses**

- get the first few rows of the dataframe: `head(), tail()`
- get the descriptive statistics of data:
  - `describe()` for numericals
  - `describe(include='object')` for text

**Get the values of columns and rows**

- get the values of a column:
  - `df['column_name']`
- get the values of several columns (replace column_name with a list of column names)
  - `df[['col1','col2']]`
- get the values of a row (here we replace row_index with an integer)
  - `df.loc[row_index]`
- get the values of several rows (replace row_index with a list of row indices)
  - `df.loc[[row_index1, row_index2]]`
- get the values of a cell:
  - `df.loc[row_index, column_name]`
- get the values by IDs:
  - cell: `df.iloc[row_id, col_id]`
  - column: `df.iloc[:, col_id]`
  - row: `df.iloc[row_id, :]`

**Get the values of a column by conditions**

- get the values of a column by conditions:
  - `df[df['column_name'] == value]`

**Get the unique values of a column**

- get the unique values of a column:
  - `df['column_name'].unique()`

**Get the number of unique values of**

get the unique values of a column

get the unique values of a column

get the number of unique values of a column

### References

[Pandas for Data Science in 20 Minutes | Python Crash Course](https://youtu.be/tRKeLrwfUgU)
