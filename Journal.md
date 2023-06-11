# 星期二, 五月 30 2023

- MEMO 14:00: drafted pandas tutorial based on the crash course from Nick xxx
- MEMO 23:04: installed glow for viewing pretty markdown files directly from terminal, which is so convenient and cool!
- MEMO 00:30: chainlit github user created three repos for chainlit project, cookbook and docs respectively.

## Tasks

- [x] 2023 年 5 月 30 日 - Task: Review chainlit documents & sample projects (done: 2023-05-31 00:05)
- [x] 2023 年 5 月 30 日 - Task: Learn the basic CRUD operations in pandas (done: 2023-05-30 23:05)

## Notes

- NOTE: [chainlit basics](30/chainlit_basics.md)
- NOTE: [pandas tutorial](30/pandas_basic.md)
- NOTE: [my thoughts](30/my_thoughts.md)


## Chainlit Basics QA

### Q1: How to upload a pdf file and load it for langchain?

```python
# demo codes
import tempfile
from langchain.document_loaders import PyPDFLoader

if action.value == 'upload_pdf_file':
    pdf_file = cl.ask_for_file(
        title='Upload a pdf file', accept=['application/pdf'], max_size_mb=10)

    temp_file = NamedTemporaryFile()
    temp_file.write(pdf_file.content)
    loader = PyPDFLoader(temp_file.name)

    documents = loader.load_and_split(text_splitter=text_splitter)
    content = documents[0].page_content

cl.send_message(content=content)
```

Key takeaways:

- using `cl.ask_for_file` function loading file
- specify `accept=['application/pdf']` to allow selection of pdf files only
- using _tempfile_ package to bridge cl.ask_for_file()) with pypdf
  - PyPDFLoader requires a file path, but chainlit only loads pdf to memory but not saves it to local folder.
  - `tempfile.write(pdf_file.content)` will save pdf content into a temp file with random name. With it assistance, pypdf now gets a path of tempfile for loading

### Q2 How do the several langchain decorators work differently?

- `@lanchain_factory` wraps up a chain or agent of langchain and returns its object. Note that its decorated function doesn't send messages to UI
- `langchain_run(agent, prompt:TypedDict)` provides a chance of doing something before agent/chain runs a prompt. The prompt is a TypedDict with question & text two keys.
- `langchain_postprocess(message:TypedDict)` provides a chance to edit the output of agent/chain before it's sent to UI. If @langchain_run decorator is implemented, this postprocess decorator is not necessary for it can be the second part of run decorate following the execution of agent.

### Q3 Which element types are supposed in the current Chainlit?

Only Text and Image (LocalImage/RemoteImage).

`name=` property is used to expose elements as access point in side/page display (not affecting inline display)

### Q4 Anything special with action_callback()?

- Action() class creates actions, whose `name=` property works like a class name, and `value=` property works like _id_ that differentiates multiple actions of same class. `label=` property is used to change text on the action link
- @action_callback takes one str parameter that specifies an action name


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


## My thought today

### Why using VSCode Journal?

As a core merit, VSCode Journal enables me to use VSCode as **the** single editor for all editing tasks

### What about the Hello World repo @github?

- VSCode Journal is a good replacement of my hello world project.
- Or maybe I should figure out how to add this Journal folder to my hello world repo on github.


# 星期三, 五月 31 2023

- MEMO 23:38: With langchain and transformers, especially given the superintelligence of GPT models, it seems not very much needed to learn spaCy unless there's a perfect task for it.
- MEMO 22:07: wrote a python script that can group employees by functional leaders
- MEMO 20:16: watched Jensen Huang's kickoff speech on COMPUTEX

## Tasks

- [>] 2023 年 5 月 31 日 - Task: learn Chapter3: Fine-tuning a Pretrained Model of NLP coures @hf.com (moved: 2023-06-01)
- [x] 2023 年 5 月 31 日 - Task: read documents of vscode journal and vscode journal view (done: 2023-05-31 20:05)
- [>] 2023 年 5 月 31 日 - Task: finish watching Andrej Karpathy's speech titled "State of GPT" (moved: 2023-06-01)
- [x] 2023 年 5 月 31 日 - Task: complete a spaCy crash course (moved: 2023-06-01)
- [x] 2023 年 5 月 31 日 - Task: comprehend all parameters in Chainlit LLMSettings (done: 2023-05-31 22:05)

## Notes

- NOTE: [llmsettings](31/llmsettings.md)
- NOTE: [computex](31/computex.md)
- NOTE: [HuggingFace NLP Course](https://huggingface.co/learn/nlp-course/chapter3)
- Note: [State of GPT](31/stateofgpt.pdf) source: https://karpathy.ai


## computex

Big Ideas:

1. This wave of AI is driving by two major movements:
   a. Accelerated Computing
   b. Generative AI
2. Data center will be the new computer.
3. Accelerated Computing is meeting its turning point.
4. AGI + Digital Twins will reshape the heavy industry. Nvidia is providing Ominiverse to facilitate manufacturers to hug AGI.


## llmsettings

_Q1: What's the difference between temperature and top p?_

A: Temperature and top-p are two different methods used in large language models to generate text.

Temperature is a hyperparameter that controls the randomness of the generated text. A higher temperature value will result in more diverse and unpredictable text, while a lower temperature value will result in more conservative and predictable text.

On the other hand, top-p (or nucleus) sampling is a method that selects the most probable words from the model's output distribution, up to a certain probability threshold. This method ensures that the generated text is diverse but still coherent and relevant to the context.

In summary, temperature controls the randomness of the generated text, while top-p sampling controls the diversity and relevance of the generated text

_Q2: How do the presence penalty and frequency penalty affect model?_

Frequency penalty and presence penalty are two parameters used in language models, such as GPT-3, to control the diversity and repetition of generated text.

Frequency penalty is a value that is added to the log-probability of a token each time it occurs in the generated text. A higher frequency penalty value will discourage the model from repeating the same words or phrases too frequently within the generated text.

Presence penalty, on the other hand, is a one-time, additive contribution that applies to all tokens that have been sampled at least once. It does not consider how frequently a word has been used, but just if the word exists in the text. The presence penalty increases the likelihood that the model will talk about new topics.

In summary, frequency penalty is used to prevent word repetitions, while presence penalty is used to prevent topic repetitions


# 星期四, 六月 01 2023

## Tasks

- [] 2023 年 5 月 31 日 - Task: 2023 年 5 月 31 日 - Task: learn Chapter3: Fine-tuning a Pretrained Model of NLP coures @hf.com
- [x] 2023 年 5 月 31 日 - Task: 2023 年 5 月 31 日 - Task: finish watching Andrej Karpathy's speech titled "State of GPT" (done: 2023-06-01 21:06)

## Notes


# 星期五, 六月 02 2023

## Tasks

- [x] 2023 年 6 月 2 日 - Task: take a crash course of numpy to learn CRUD operations (done: 2023-06-02 16:06)

## Notes

- NOTE: [numpy basics](02/numpy_basics.md)


## Numpy basics

Numpy makes the vector/matrix calculation as easy as number calculation.

### CRUD operations

#### Create

Numpy provides a bunch of convenient functions for creating a ndarray with a default element dtype of int64.

##### 1. Create a ndarray filled with same number

`np.zeroes(tuple), .ones(tuple), .full(tuple, n)`

- tuple: taking a tuple parameter to specify the shape (sizes of dimensions)
- n: creating an array filled with 0, 1, or n

##### 2. Create a ndarray with random numbers

`np.random.random(size)`: returns a list of random float64 (1-dimension)
`np.random.rand(d1, d2, d3, ...)`: returns random float64 in multi-dimensions

`np.random.randint(low, high, size, dtype)`: returns a list of integers in dtype with a value range of [low, high)

##### 3. Convert a python list to ndarray

`np.array(list1)`

#### Read

Numpy supports slicing given the array attribute, which can be retrieved from a few properties:

data.shape - returns the shape of ndarray
data.size - returns the total number of elements in the array
data.dtype - returns the data type (dtype) of the array elements
type(data) - returns numpy.ndarray

#### Update

The purpose of introducing numpy is to do vector math. Numpy provides functions for basic arithmetic operations

- np.add(list1, list2): returns the sum of two lists
- np.subtract(list1, list2)
- np.multiply(list1, list2)
- np.divide(list1, list2)
- np.divmod(list1, list2): turns two ndarrays for quotients and remainders respectively
- np.dot(list1, list2): returns the dot product of two lists

Or even sipmler form, just use +, -, \*, /, % operators.

also other mathematical operations, such as abs(), exp(), log(), sqrt(), power(), min(), max() etc.

Finally, data manipulation functions like insert(), append(), sort(), and reshape().

#### Delete

- np.delete(data, index, axis): delete data specified by index and axis (=1 for row and =0 for column)
- np.save("filename", data): save data to local npy file
- np.load("filename"): load data from npy file

#### Pandas vs. Numpy

##### What are the differences?

The dataframes in pandas are 2-dimentional data structure, and series are one-dimentional.

- dataframes/series have index & column names, which numpy ndarrays don't have.
- ndarrays can do fast vector/matrix calculations, which pandas can't do.

##### How to convert between the two?

- dataframe or series to ndarray: df.values, or df.to_numpy()
- ndarray to dataframe: pd.dataframe(arr, columns=[...])


# 星期三, 六月 07 2023

## Tasks

- [x] 2023 年 6 月 7 日 - Task: Get basic knowledge about plotly (done: 2023-06-08 00:06)

## Notes

- NOTE: [Plotly Basic Introduction](./07/plotly.ipynb)


## Plotly in Python basics

### Quick Facts

- `Plotly for Python` is a graphing library free of charge and licensed under the MIT license
- `Dash` is an analytic app in Python using Plotly figures. It's also free and licensed under the MIT license
- Plotly library is supported in Jupyter Notebook, JupyterLab, Dash and even Streamlit
- Plotly Express vs. Gragh Objects:
  - `Plotly Express` functions, as the recommended method, use Plotly graph objects internally and return a `plotly.graph_objects.Figure` instance
  - `Plotly Graph Objects` provide a low level interface for developing custom visualization
- The best way of using Plotly charts is to always look for needed charts from the [online demo library](https://plotly.com/python/)

### More Info

- [ ] [Displaying plotly chart in Streamlit](https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart)
- [ ] [Code Example: Plotly Chart in Streamlit](./plotly_st.py)
- [ ] [Plotly Express API Reference](https://plotly.com/python-api-reference/plotly.express.html)
- [ ] [Demo Charts: Plotly Graphing Library for Python](https://plotly.com/python/)


# 星期四, 六月 08 2023

- MEMO 14:52: pydantic enforces type hints at runtime, and it provides friendly errors to users for invalid types
- MEMO 14:27: postman is used to simulate client browser and provide users friendly errors when data is invalid
- MEMO 14:02: learn some basics of FastAPI

## Tasks

- [x] 2023 年 6 月 8 日 - Task: write a python program that automates the calculation of monthly OT/Pager Comp report data (done: 2023-06-08 22:06)

## Notes

- NOTE: [sqlite3 basics](08/sqlite3_basics.md)
- NOTE: [pagercalc.py](08/pagercalc.py) use pandas to calculate monthly compensation report
- NOTE: [fastapi basics](08/fastapi_basics.md)
- NOTE: [fastapi demo (main.py)](08/main.py)
- NOTE: [Pydantic document reference](https://docs.pydantic.dev/latest/)


## fastapi basics

- API's in essence are about Path Operations, supported by HTTP methods.


## sqlite3 basics

### Basics

Concepts:

- cursor
- transactions

Functions:

- `sqlite3.connect(db)` to create a db
- `con.cursor()` to return a cursor for accessing a db
- `cur.execute(sql)` to execute one sql statement
- `cur.executemany(sql, list)` to execute many transactions with the aid of ? placeholder
- `con.commit()` to commit the transactions
- `res.fetchone() & res.fetchall()` to fetch one row or all rows in the result set

### SQL STATEMENTS

- CREATE TABLE <table_name> (...)
- SELECT ... FROM <table_name>
- INSERT INTO ... VALUES (...)

SQL SUBCLAUSES:

- WHERE
- ORDER BY
- GROUP BY

### Data Types

| SQLite type | Python type                             |
| :---------- | :-------------------------------------- |
| NULL        | None                                    |
| INTEGER     | int                                     |
| REAL        | float                                   |
| TEXT        | depends on text_factory, str by default |
| BLOB        | bytes                                   |

### Sqlite3 Built-in Features

- [sqlite_master](https://www.sqlite.org/schematab.html): every SQLite database contains a single "schema table" that stores the schema for that database

### Security

- SQL injection attacks

### References

- [ ] [Sqlite3 Python Docs](https://docs.python.org/3/library/sqlite3.html)


# 星期五, 六月 09 2023

## Tasks

- [x] 2023 年 6 月 9 日 - Task: updated overtime.py to store data in sqlite3 db (done: 2023-06-09 17:06)

## Notes

- Note: [overtime.py](./09/overtime.py) is a python module for managing overtime records and db
- Note: [demo.ipynb](./09/demo.ipynb) is a demo notebook that uses overtime module to process overtime data


# 星期六, 六月 10 2023

## Tasks

## Notes

- NOTE: [fastapi002](10/fastapi002.md) follows the [fastapi basics](08/fastapi_basics.md).


## fastapi002

... following the basic tutorials on Jun 08.

### Path parameter

`@app.get("/posts/{id}")`

In the code snippet above, "id" is a path parameter which passes an id in the request.

Key points:

1. this path parameter can be used in a GET method.
2. a pair of curly brackets is used to mark a path parameter.
3. the type of path parameters is always `str`, and so you might need to do type conversion manually.


# 星期日, 六月 11 2023

- MEMO 13:07: [Data School](https://www.youtube.com/@dataschool) is a youtube channel that introduces data science to beginners. What it does great in my opinion is that:
  - the intructor will teach the best practices of coding and demonstrate both good behaviors and bad behaviors. Therefore, the audience will learn the decent way.
  - secondly, the instructor's english is clear and speed is slow, makin the videos friendly to foreign learners.

## Tasks

- [] 2023 年 6 月 11 日 - Task: Figure out the differences between .loc, .iloc and .ix in using pandas dataframe

## Notes

- NOTE: [dataschool@youtube: Best Practices with Pandas](https://www.youtube.com/watch?v=hl-TGI4550M&list=PL5-da3qGB5IBITZj_dYSFqnd_15JgqwA6)


## journal book project

### Description

This project is to merge all journal markdowns into a single file. It'll take a few steps:

1.  Read all the markdown files in the journal folder.
2.  Write these markdown files into a single output file.

### Notes

Alternative steps: 2. Parse the markdown files into a list of dictionaries. 3. Sort the list of dictionaries by date. 4. Write the list of dictionaries to a markdown file.


