from simple_http_server import route, server
    
# @route("/")
# def index():
#     return {"hello": "world"}   


# @route("/about")
# def about():
#     return {"about": "I am About"}   


server.start(port=9090)