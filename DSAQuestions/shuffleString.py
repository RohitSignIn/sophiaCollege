# 1528. Shuffle String

# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

def shuffleString(s, indices):

    dummyList = [None] * len(s)
    i = 0
    while( i<len(s)):
        char = s[i]
        belongsto = indices[i]
        dummyList[belongsto] = char
        i+=1

    res = ""
    for i in dummyList:
        res = res + i

    return res

print(shuffleString("codeleet", [4,5,6,7,0,2,1,3]))
