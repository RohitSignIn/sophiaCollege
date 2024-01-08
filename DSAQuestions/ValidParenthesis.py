# 2. Valid Parenthesis: https://leetcode.com/problems/valid-parentheses/description/
def validParentheses(s):
    st = []
    allParentheses = {
        "(": ")",
        "[": "]",
        "{": "}" 
    }

    for i in s:
        if(len(st) == 0):
            st.append(i)
        else:
            lastVal = st.pop()
            if(i != allParentheses[lastVal]):
                st.append(lastVal)
                st.append(i)

    if(len(st)):
        return False
    return True


s = "()[]{}"
print(validParentheses(s))

