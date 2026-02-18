def isPalindrome(x):
    if x < 0:
        return False
    res = list(map(int, str(x)))
    i = 0
    n = len(res)-1
    while i < n:
        if res[i] != res[n]:
            return False
        i += 1
        n -=1
    return True




print(isPalindrome(1204022221))