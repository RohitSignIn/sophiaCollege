# 28. Find the Index of the First Occurrence in a String

def find_first_occurrence(haystack, needle): 
    i = 0
    j = 0
    pos = -1
    while(i < len(haystack) and j < len(needle)):
        if(haystack[i] == needle[j]):
            if(pos == -1):
                pos = i
            i+=1
            j+=1
        else:
            pos = -1
            j=0
            i+=1
    return pos

haystack = "sadbutsad"
needle = "sad"


print("First Occurence", find_first_occurrence(haystack, needle))