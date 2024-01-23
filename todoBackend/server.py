from simple_http_server import server
from simple_http_server import PathValue
from simple_http_server import request_map

import main
    
# USER Api START 

@request_map("/api/v1/user/{id}", method="GET")
def index():
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


# USER Api END


server.start(port=9090)