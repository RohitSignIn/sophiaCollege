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


def reorderLinkedList(list1):
    p1 = list1
    p2 = list1
    while(p2["next"] != None and p2["next"]["next"] != None):
        p1 = p1["next"]
        p2 = p2["next"]["next"]

    list2 = p1["next"]
    p1["next"] = None

    printList(list1)
    printList(list2)

    return



list1 = None

list1 = addAtHead(list1, 6)
list1 = addAtHead(list1, 5)
list1 = addAtHead(list1, 4)
list1 = addAtHead(list1, 3)
list1 = addAtHead(list1, 2)
list1 = addAtHead(list1, 1)

reorderLinkedList(list1)