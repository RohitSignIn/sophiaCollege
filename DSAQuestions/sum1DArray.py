def sumArray(nums):
    i=1
    while(i<len(nums)):
        nums[i] = nums[i] + nums[i-1]
        i+=1

    return nums

print(sumArray([1,2,3,4]))