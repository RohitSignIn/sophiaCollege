sum = 0


def preOrderTraversal(root):
    global sum
    if(root == None):
        return
    
    sum += root["data"]
    preOrderTraversal(root["left"])
    preOrderTraversal(root["right"])

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

preOrderTraversal(root)
print(sum)