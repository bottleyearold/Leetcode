def hasAllCodes(s, k):
    req = 2**k
    back_counter = 0
    count = set()
    for i in range(k,len(s)+1):
        count.add(s[back_counter:i])
        back_counter+= 1
    if len(count) == req:
        return True 
    else:
        return False

print(hasAllCodes('0110', 2))