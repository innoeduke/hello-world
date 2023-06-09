# sqlite3 basics

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
