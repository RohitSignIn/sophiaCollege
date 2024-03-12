def inOrderTraversal(root):
    if(root == None):
        return
    
    inOrderTraversal(root["left"])
    print(root["data"])
    inOrderTraversal(root["right"])

root = {
    "data": 2,
    "left": {
    "data": 4,
    "left": {
    "data": 8,
    "left":None,
    "right":None,
    },
    "right": {
    "data": 6,
    "left": None,
    "right": None
},
},
    "right": {
    "data": 3,
    "left": {
    "data": 1,
    "left": None,
    "right": None
},
    "right": None
},
}

inOrderTraversal(root)