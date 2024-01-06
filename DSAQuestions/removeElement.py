# Remove Element

def removeElement(nums, val):
    k = 0
    for i in nums:
        if(i == val):
            continue
        k+=1
    
    return k

nums = [0,1,2,2,3,0,4,2] 
val = 2

print(removeElement(nums, val))
