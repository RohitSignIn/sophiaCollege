def singleNonDuplicate(nums):
    n = len(nums)
    start = 0
    end = n-1

    while(start < end):
        mid = int((start + end) / 2)

        if(mid == 0 and nums[mid] != nums[mid+1]):
            return mid
        if(mid == n-1 and nums[mid] != nums[mid-1]):
            return mid
        
        if(mid != 0 and mid != n-1 and nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]):
            return mid
        
        # if(mid == 0):

        # if(mid == n-1):

        if(nums[mid] == nums[mid-1]):
            if(mid & 1):
                start = start + 1
            else:
                end = end - 2
        else:
            if(mid & 1):
                end = end - 1
            else:
                start = start + 2


print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))