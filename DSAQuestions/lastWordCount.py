# LEETCODE : https://leetcode.com/problems/length-of-last-word/


def lengthOfLastWord(self, s: str) -> int:
    lastWordCount = 0
    flag = True
    for i in s:
        if(i == " "):
            flag= True
            continue
        else:
            if(flag):
                lastWordCount = 1
                flag= False
            else:
                lastWordCount += 1
        
    return lastWordCount