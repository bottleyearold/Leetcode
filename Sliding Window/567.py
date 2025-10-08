
        
# def checkInclusion(s1, s2):
#     j = 0
#     end = len(s1)
#     s1_sort = sorted(list(s1))
#     for i in range(end, len(s2)+1):
#         if set(s2[j:i]) == set(s1):
#             if sorted(list(s2[j:i])) == s1_sort:
#                 return True
#         j+=1
#     return False


def checkInclusion(s1,s2):
    s1_hash = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    s2_hash = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    matches = 0
    for i in s1:
        s1_hash[i] += 1

    for i in range(0,len(s1)):
        s2_hash[s2[i]] += 1
    
    for key,value in s1_hash.items():
        if s1_hash[key] == s2_hash[key]:
            matches += 1

    if matches == 26:
        return True 
    
    left = 0
    for right in range(len(s1),len(s2)):

        inn = s2[right]
        out = s2[left]

        if s2_hash[inn] == s1_hash[inn]:
            matches -= 1
        s2_hash[inn] += 1
        if s2_hash[inn] == s1_hash[inn]:
            matches += 1

        
        if s2_hash[out] == s1_hash[out]:
            matches -=1
        s2_hash[out] -= 1
        if s2_hash[out] == s1_hash[out]:
            matches +=1

        left += 1
        print(matches)
        if matches == 26:
            return True 
    
    print(matches)
    return False

    
print(checkInclusion(s1 = "vxq", s2 = "sfslnheghnbhhpgxxxxxxxzkxxxxyqvxqmnikljmmcrleffce"))


