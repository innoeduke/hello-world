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

- get the values by labels

  - `df.loc[row_indices, col_names]`
  - note that labels are inclusive

- get the values by positions:

  - `df.iloc[row_range, col_range]`
  - note that right edge is exclusive

- get the values by mix of labels and positions
  - `df.ix[row_indices|row_range, col_names|col_range]`

**Get the values of a column by conditions**

- get the values of a column by conditions:
  - `df.loc[:, df['column_name'] == value]`

**Get the unique values of a column**

- get the unique values of a column:
  - `df.loc[:, 'column_name'].unique()`

**Get the number of unique values of**

get the unique values of a column

get the unique values of a column

get the number of unique values of a column

### References

[Pandas for Data Science in 20 Minutes | Python Crash Course](https://youtu.be/tRKeLrwfUgU)
