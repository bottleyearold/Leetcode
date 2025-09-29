
def countGoodSubstrings(s):
    counter = 0

    if len(s) < 3:
        return 0

    for i in range(0, len(s)-2):
        if s[i] not in s[i+1] and s[i+1] not in s[i+2] and s[i] not in s[i+2]:
            counter += 1
    return counter
print(countGoodSubstrings("aababcabc"))


        



