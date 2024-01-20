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


def addNodeatTail(head, node):
    if(head == None):
        return node
    
    node["next"] = None

    temp = head 
    while(temp["next"] != None):
        temp = temp["next"]

    temp["next"] = node
    return head

def reorderLinkedList(list1):
    # Step 1 Splitting in two Linked List
    p1 = list1
    p2 = list1
    while(p2["next"] != None and p2["next"]["next"] != None):
        p1 = p1["next"]
        p2 = p2["next"]["next"]

    list2 = p1["next"]
    p1["next"] = None

    # Step 2 Reverse second List 
    st = []
    while(list2 != None):
        st.append(list2)
        list2 = list2["next"]

    list2 = None
    while(len(st)):
        node = st.pop()
        list2 = addNodeatTail(list2, node)

    # step 3
    p1 = list1 
    p2 = list2 

    turn = True
    while(p2 != None):
        if(turn):
            ref = p1["next"]
            p1["next"] = p2
            p1 = ref
            turn = False 
        else:
            ref = p2["next"]
            p2["next"] = p1
            p2 = ref
            turn = True 

    return list1
                

list1 = None

# list1 = addAtHead(list1, 6)
list1 = addAtHead(list1, 5)
list1 = addAtHead(list1, 4)
list1 = addAtHead(list1, 3)
list1 = addAtHead(list1, 2)
list1 = addAtHead(list1, 1)

printList(reorderLinkedList(list1))