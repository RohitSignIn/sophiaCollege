def f(r1, r2):
    if (r1 == None and r2 == None):
        return True
    if (r1 == None):
        return False
    if(r2 == None):
        return False

    return r1["val"] == r2["val"] and f(r1["left"], r2["right"]) and f(r1["right"], r2["left"])
    

def isSymmetric(root):
    return f(root, root)


root = {
    "val": 1,
    "left": {
    "val": 2,
        "left": {
            "val": 3,
            "left": None,
            "right": None,
        },
        "right": {
            "val": 4,
            "left": None,
            "right": None,
        },
    },
    "right": {
        "val": 2,
            "left": {
            "val": 4,
            "left": None,
            "right": None,
    },
    "right": {
    "val": 3,
    "left": None,
    "right": None,
},
},
}

print(isSymmetric(root))