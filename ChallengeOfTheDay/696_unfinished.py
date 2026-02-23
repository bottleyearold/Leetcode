def countBinarySubstrings(s):
    one_pointer = s[0]
    count_dict = {0:0, 1:0}
    counter = 0
    initial  = True
    for i in range(0,len(s)):
        #add to correct dictonary 
        count_dict[int(s[i])] += 1


        if one_pointer != s[i] and count_dict[one_pointer] >0 and not initial:
            counter += 1 
            count_dict[one_pointer] -= 1

        #second instance of a number 
        if one_pointer == s[i] and not initial:
            count_dict[one_pointer] == 1
            one_pointer = s[i-1]
            count_dict[one_pointer] -= 1
            counter += 1
            initial = False

    return counter 

print(countBinarySubstrings("0101010011000000"))       