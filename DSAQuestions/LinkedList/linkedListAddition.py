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

list1 = None
list1 = addAtHead(list1, 3)
list1 = addAtHead(list1, 4)
list1 = addAtHead(list1, 2)

list2 = None
list2 = addAtHead(list2, 4)
list2 = addAtHead(list2, 6)
list2 = addAtHead(list2, 5)


printList(getAdditon(list1, list2))