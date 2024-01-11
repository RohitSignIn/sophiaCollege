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


def getIntersection(list1, list2):
    l1Len = getLength(list1)
    l2Len = getLength(list2)

    diff = abs(l1Len-l2Len)

    if(l1Len > l2Len):
        while(diff):
            list1 = list1["next"]
            diff -= 1
    else:
        while(diff):
            list2 = list2["next"]
            diff -= 1

    while(list1 !=None):
        if(list1 == list2):
            return list1
        list1 = list1["next"]
        list2 = list2["next"]

    return "No Intersection"

list1 = None
list1 = addAtHead(list1, 1)
list1 = addAtHead(list1, 2)

list4 = None
list4 = addAtHead(list4, 1)
list4 = addAtHead(list4, 2)

list2 = None
list2 = addAtHead(list2, 3)
list2 = addAtHead(list2, 4)
list2 = addAtHead(list2, 5)

list3 = None
list3 = addAtHead(list3, 6)
list3 = addAtHead(list3, 7)
list3 = addAtHead(list3, 8)

t1 = list1
t2 = list2

while(t1["next"] != None):
    t1 = t1["next"]
while(t2["next"] != None):
    t2 = t2["next"]

t1["next"] = list3
t2["next"] = list3
        
print(getIntersection(list1, list2))