def hasAlternatingBits(n):
    binary = bin(n)
    last = binary[2]
    if len(binary) == 3:
        return True
    for i in range(3, len(binary)):
        if last == binary[i]:
            return False
        last = binary[i]
    return True 

print(hasAlternatingBits(3))