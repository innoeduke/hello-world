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
