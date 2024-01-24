from simple_http_server import server
from simple_http_server import PathValue
from simple_http_server import request_map

import main
    
# USER Api START 

# Get Users
@request_map("/api/v1/users", method="GET")
def index():
    res = main.getUsers()
    return {
        "status_code": 200,
        "success": True,
        "message": "Fetch All successfully",
        "data": res
    }

# Get User 
@request_map("/api/v1/user/{id}", method="GET")
def index(id=PathValue()):
    res = main.getUser(id)
    return {
        "status_code": 200,
        "success": True,
        "message": "Fetch successfully",
        "data": res
    }

# Create User
@request_map("/api/v1/user", method="POST")
def index(username, password):
    main.addUser(username, password)
    return {
        "status_code": 201,
        "success": True,
        "message": "Todo Added successfully",
        "data": []
    }

# Update User
@request_map("/api/v1/user", method="PUT")
def index(update, to, userId):
    res = main.updateUser(update, to, userId)
    return {
        "status_code": 201,
        "success": True,
        "message": "Update successfully",
        "data": res
    }

# DELETE User
@request_map("/api/v1/user", method="DELETE")
def index(userId):
    res = main.removeUser(userId)
    return {
        "status_code": 201,
        "success": True,
        "message": "Remove successfully",
        "data": res
    }
# USER Api END


# Todo Api START 
# Get All Todos
@request_map("/api/v1/todos", method="GET")
def index():
    res = main.getTodos()
    return {
        "status_code": 200,
        "success": True,
        "message": "Fetch All successfully",
        "data": res
    }

# Get Todo by todoId
@request_map("/api/v1/todo/{id}", method="GET")
def index(id = PathValue()):
    res = main.getTodo(id)
    return {
        "status_code": 200,
        "success": True,
        "message": "Fetch successfully",
        "data": res
    }

# Get Todo by userId
@request_map("/api/v1/usertodo/{id}", method="GET")
def index(id = PathValue()):
    res = main.getUserTodo(id)
    return {
        "status_code": 200,
        "success": True,
        "message": "Fetch successfully",
        "data": res
    }

# Create Todo
@request_map("/api/v1/todo", method="POST")
def index(task, userId):
    main.addTodo(task, userId)
    return {
        "status_code": 201,
        "success": True,
        "message": "Todo Added successfully",
        "data": []
    }

# Update Todo by todoId
@request_map("/api/v1/todo", method="PUT")
def index(update, to, todoId):
    res = main.updateTodo(update, to, todoId)
    return {
        "status_code": 201,
        "success": True,
        "message": "Updated successfully",
        "data": res
    }

# DELETE todo by todoId
@request_map("/api/v1/todo", method="DELETE")
def index(todoId):
    res = main.removeTodo(todoId)
    return {
        "status_code": 201,
        "success": True,
        "message": "Remove successfully",
        "data": res
    }
# USER Api END


server.start(port=9090)