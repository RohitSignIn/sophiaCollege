# // Minimize the integer


# // Problem Statement

# // Antonio got a very large integer as his christmas present from his parents. Antonio does not like large integers and hence decided to change a few digits of this integer and make it as small as possible.

# // But changing too many digits will make Antonio’s parents sad. More formally if Antonio changes more than K digits of the integer, his parents will become sad. Antonio does not want that to happen and hence will change at most K digits of the given integer.

# // Also if the final integer contains any leading zeroes, Antonio’s parents again become sad. So Antonio will perform the K changes in such a way that the final integer does not contain any leading zeroes.

# // Given the integer Antonio got and K(maximum number of changes Antonio can perform), print the minimum integer that Antonio can get.
 

# // Input Format

# // First line contians a single integer denoting the integer Antonio got as his christmas present.
# // Next line contains a single integer denoting K.
 

# // Output Format

# // Print the minimum integer that Antonio can get.
# // Constraints

# // 1<=number of digits in the integer<=10^5
# // 1<=K<=number of digits in the integer
# // Its guaranteed that the given integer does not contain any leading zeros.
 

# // Sample Input 1

# // 299

# // 2

 

# // Sample Output 1

# // 1099


# // Explanation of Sample 1

# // Antonio can change the first digit to ‘1’ and change the second digit to ‘0’. It can be proved that 1099 is the minimum possible integer that Antonio can get.


# no = "1034"
# noStr = [char for char in no]
# k = 2

# count = 0
# while(k > 0):
#     if(count == 0 and noStr[count] != "1"):
#         noStr[count] = "1"
#         k = k-1
#     elif(count != 0 and noStr[count] != "0"):
#         noStr[count] = "0"
#         k = k-1

#     count = count+1

# noStr = "".join(noStr)

# print(noStr)

no = [2,0,2,3]
k = 2

count = 0
while(k > 0):
    if(count == 0 and no[count] != 1):
        no[count] = 1
        k -= 1
    elif(count != 0 and no[count] != 0):
        no[count] = 0
        k -= 1
    count += 1

print(no)