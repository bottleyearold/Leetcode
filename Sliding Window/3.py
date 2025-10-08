def lengthOfLongestSubstring(s):
    left = 0
    values = []
    unique_substring_vals = []

    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1


    for i in range(0,len(s)):

        if s[i] not in values:
            values.append(s[i])
        else:
            if s[i] == values[0]:
                left += 1
                unique_substring_vals.append(len(values))
                del values[0]
                values.append(s[i])
            else:
                unique_substring_vals.append(len(values))
                left = values.index(s[i]) + 1
                del values[0:left]
                values.append(s[i])
    unique_substring_vals.append(len(values))
    if unique_substring_vals == []:
        return len(s)
    return max(unique_substring_vals)
                


print(lengthOfLongestSubstring("bbbbb"))


