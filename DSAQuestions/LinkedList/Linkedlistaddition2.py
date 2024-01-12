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

def getLength(head):
    temp = head
    count = 0
    while(temp != None):
        count += 1
        temp = temp["next"]

    return count

def getAdditon(list1, list2):
    list3 = None
    carry = 0
    while(list1 != None and list2 != None):
        data = list1["data"] + list2["data"] + carry
        carry = data//10
        data = data % 10
        list3 = addAtTail(list3, data)
        list1 = list1["next"]
        list2 = list2["next"]


    while(list1 != None):
        data = list1["data"] + carry
        carry = int(data%10)
        data = data // 10
        list3 = addAtTail(list3, data)
        list1 = list1["next"]

    while(list2 != None):
        data = list2["data"] + carry
        carry = int(data%10)
        data = data // 10
        list3 = addAtTail(list3, data)
        list2 = list2["next"]


    return list3


def reverseList(head):
    temp = head
    newList = None
    while(temp!=None):
        newList = addAtHead(newList, temp["data"])
        temp = temp["next"]

    return newList
head = None

head = addAtHead(head, 5)
head = addAtHead(head, 4)
head = addAtHead(head, 3)
head = addAtHead(head, 2)
head = addAtHead(head, 1)

printList(head)
printList(reverseList(head))