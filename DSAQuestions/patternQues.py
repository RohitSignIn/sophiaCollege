# Pattern Question

# 1).
#    *
#   **
#  ***
# ****
# 1
# 2
# 3
# 4

n = 8
for i in range(n,0,-1):
    spaces = n - i
    while(spaces):
        print(" ", end="")
        spaces -= 1

    for j in range(0,i):
        print("*", end="")

    print("")


# 2).
# ****
#  ***
#   **
#    *


# 3).
# ****
# *  *
# *  *
# ****
    
n = 8   
for i in range(1, n+1):

    if(i == 1 or i == n):
        for j in range(1,n+1):
            print("*", end="")
        print("")
    else:
        for j in range(1,n+1):
            if(j == 1 or j == n):
                print("*", end="")
            else:
                print(" ", end="")
        print("")



# 4).
# ******* 4 0 
#  *****  3 1
#   ***   2 2
#    *    1 3


# 5).
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
    

# 6).
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******
    
# 7).
#    *
#   ***
#  *****
# *******
#   ***
#   *** 
    
# 8).
#    1
#   222
#  33333
# 4444444

# 9).
#    1
#   121
#  12321
# 1234321

# 10). 
#    1
#   123
#  12345
# 1234567

# 11).
#    a
#   aba
#  ababa
# abababa

# 12).
#    a
#   bab
#  ababa
# bababab
