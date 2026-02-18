#NOT DONE


def characterReplacement(s, k):
    #B-->A s = "ABAB" k = 2
    l = 0 
    k_count = 0
    first_letter = s[0]
    m = [] #this will hold very instance of values 
    m_count = 0
    res = []

    for r in range(len(s)):
        if s[r] != first_letter:
            k_count += 1
            second_letter = s[r]
            m.append(r+1)
        if k_count > k:
            res.append(r-l)
            l = m[m_count]
            m_count += 1
            k_count -=1
    if res == []:
        return len(s)
    res.append(r-l+1)


    l = 0 
    k_count = 0
    first_letter = s[0]
    m = [] #this will hold very instance of values 
    m_count = 0
    res_1 = []

    for r in range(len(s)):
        if s[r] != second_letter:
            k_count += 1
            m.append(r+1)
        if k_count > k:
            res_1.append(r-l)
            l = m[m_count]
            m_count += 1
            k_count -=1
    if res_1 == []:
        return len(s)
    res_1.append(r-l+1)

    return max(max(res_1),max(res))

print(characterReplacement("AABABBA",1))