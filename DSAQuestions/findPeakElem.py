def peakElement(arr):
    n = len(arr)
    start = 0
    end = n-1
    while(start < end):
        mid = int((start + end)/2)

        if(mid == 0 and arr[mid+1] < arr[mid]):
            return mid
        
        if(mid == n-1 and arr[mid-1] < arr[mid]):
            return mid
        
        if(mid != 0 and mid != n-1 and arr[mid+1] < arr[mid] and arr[mid-1] < arr[mid]):
            return mid
        
        if((arr[mid-1] - arr[mid+1]) > 0):
            end = mid-1
        else:
            start = mid+1


print(peakElement([1,2,3,1]))  
