## fastapi002

... following the basic tutorials on Jun 08.

### Path parameter

`@app.get("/posts/{id}")`

In the code snippet above, "id" is a path parameter which passes an id in the request.

Key points:

1. this path parameter can be used in a GET method.
2. a pair of curly brackets is used to mark a path parameter.
3. the type of path parameters is always `str`, and so you might need to do type conversion manually.
