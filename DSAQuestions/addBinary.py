def addBinary(a, b):
    lenA = len(a)
    lenB = len(b)
    diff = lenA - lenB
    i = 0
    carry = False
    res = ""

    if(diff < 0):
        i = lenB-1 
        while(diff < 0):
            a = "0"+a
            diff += 1
    elif(diff > 0):
        i = lenA-1 
        while(diff > 0):
                b = "0"+b
                diff -= 1

    while(i >= 0):
        if(a[i] == "0" and b[i] == "0"):
            temp = "0"
            if(carry):
                temp = "1"
                
            carry = False
            res = temp + res
        if(a[i] == "1" and b[i] == "0"):
            temp = "1"
            if(carry):
                temp = "0"

            res = temp + res
        if(a[i] == "0" and b[i] == "1"):
            temp = "1"
            if(carry):
                temp = "0"
                    
            res = temp + res
        if(a[i] == "1" and b[i] == "1"):
            temp = "0"
            if(carry):
                temp = "1"
            carry = True
                    
            res = temp + res
        i-=1

    if(carry):
        res = "1" + res

    return res

print(addBinary("1010", "1011"))


