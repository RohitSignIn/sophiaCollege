# 9. Palindrome Number

n = 121

nStr = str(n)
newStr = ""
for i in nStr:
    newStr = i + newStr

if(nStr == newStr):
    print("palindrome")