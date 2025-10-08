def findAnagrams(s, p):
    s_hash = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    p_hash = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    matches = 0
    indexes = []

    if len(p)>len(s):
        return []

    for i in p:
        p_hash[i] += 1
    
    for i in range(0, len(p)):
        s_hash[s[i]] += 1
    
    for key,value in p_hash.items():
        if s_hash[key] == p_hash[key]:
            matches += 1
    left = 0
    if matches == 26:
        indexes.append(left)
    for right in range(len(p),len(s)):

        if s_hash[s[left]] == p_hash[s[left]]:
            matches -= 1
        s_hash[s[left]] -= 1
        if s_hash[s[left]] == p_hash[s[left]]:
            matches += 1
        
        if s_hash[s[right]] == p_hash[s[right]]:
            matches -= 1
        s_hash[s[right]] += 1
        if s_hash[s[right]] == p_hash[s[right]]:
            matches += 1
        

        left += 1
        if matches == 26:
            indexes.append(left)
    return indexes

                
print(findAnagrams("cbaebabacd","abc"))