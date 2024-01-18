def createNode(data):
    return {
        "data": data,
        "next": None,
    }

def addAtHead(head, data):
    if(head == None):
        return createNode(data)
    newNode = createNode(data)
    newNode["next"] = head
    return newNode


def printList(head):
    temp = head
    while(temp != None):
        print(temp["data"], "=>", end="")
        temp = temp["next"]
    print("end")

def addAtTail(head, data):
    if(head == None):
        return createNode(data)
    
    temp = head
    while(temp["next"] != None):
        temp = temp["next"]

    newNode = createNode(data)
    temp["next"] = newNode

    return head

head = {
    "data": 1,
    "next": {
        "data": 2,
        "next": {
            "data": 3,
            "next": None
        }
    }
}

def removeAtHead(head):
    if(head == None):
        print("Head is None")
        return
    
    temp = head["next"]
    head["next"] = None

    return temp

def removeAtTail(head):
    if(head == None):
        print("Head is None")
        return
    
    temp = head

    while(temp["next"]["next"] != None):
        temp = temp["next"]

    temp["next"] = None
    return head


def mergeLinkedList(list1, list2):
    list3 = None
    while(list1 != None and list2 != None):
        if(list1["data"] < list2["data"]):
            list3 = addAtTail(list3, list1["data"])
            list1 = list1["next"]
        else:
            list3 = addAtTail(list3, list2["data"])
            list2 = list2["next"]

    while(list1 != None):
            list3 = addAtTail(list3, list1["data"])
            list1 = list1["next"]

    while(list2 != None):
            list3 = addAtTail(list3, list2["data"])
            list2 = list2["next"]

    return list3



list1 = None
list2 = None

list1 = addAtHead(list1, 4)
list1 = addAtHead(list1, 3)
list1 = addAtHead(list1, 2)
list1 = addAtHead(list1, 1)

list2 = addAtHead(list2, 5)
list2 = addAtHead(list2, 3)
list2 = addAtHead(list2, 2)

printList(mergeLinkedList(list1, list2))