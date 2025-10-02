
        
def checkInclusion(s1, s2):
    j = 0
    end = len(s1)
    s1_sort = sorted(list(s1))
    for i in range(end, len(s2)+1):
        if set(s2[j:i]) == set(s1):
            if sorted(list(s2[j:i])) == s1_sort:
                return True
        j+=1
    return False


print(checkInclusion(s1 = "hello", s2 = "ooollleeehholhe"))
