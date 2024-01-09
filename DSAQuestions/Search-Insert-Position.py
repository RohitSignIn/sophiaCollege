def SearchInsertPosition(nums, target):
    first = 0
    last = len(nums) - 1
    while(True):
        mid = (first+last) // 2

        if(nums[mid] == target):
            return mid
        elif(nums[mid] > target):
            if(nums[mid-1] < target ):
                return mid
            last = mid - 1
        else:
            first = mid + 1

nums = [1,3,5,6,7]
target = 7

print(SearchInsertPosition(nums, target))