def numOfSubarrays(arr, k, threshold):
    j = 0
    thresh = 0
    counter = 0
    for i in range(0,len(arr)):
        if i > k-2:
            thresh += arr[i]
        if i <= k-2:
            thresh += arr[i]
        else:
            if thresh/k >= threshold:
                counter += 1
            thresh -= arr[j]
            j+=1

            
    return counter


print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))
print(numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))



