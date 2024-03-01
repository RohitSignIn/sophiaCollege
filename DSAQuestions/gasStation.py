def canCompleteCircuit(gas, cost):

    n = len(gas) 
    start_station = -1
    fuel = 0
    count = 0
    i = 0

    while(count < n+n):
        if(start_station == i): 
            return i
        fuel += gas[i]

        if(fuel >= cost[i]):
            if(start_station == -1):
                start_station = i
            fuel -= cost[i]
            i = (i+1)%n
        else:
            fuel = 0
            start_station = -1
            i = (i+1)%n
        
        count+=1
    
    return -1


print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))