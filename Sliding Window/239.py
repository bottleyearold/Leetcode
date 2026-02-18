#NOT DONE

def maxSlidingWindow(nums, k):
    l = 0
    count = 0
    maxx = float('-inf')
    res = []

    if k == 1:
        return nums
    for r in range(len(nums)):
        if r < k:
            if nums[r] > maxx:
                maxx = nums[r]
                count = 1
            elif nums[r] == maxx:
                count += 1
            
            if r == k-1:
                res.append(maxx)
                if nums[l] ==maxx and count == 1:
                    print("BOOOO")
                    maxx = float('-inf')
                    for i in range(l+1,r):
                        if nums[i] > maxx:
                            maxx = nums[i]
                            count = 1
                        elif nums[i] == maxx:
                            count += 1


        else:
            # print("left: "+ str(l) + "       right: "+str(r) + "     count: "+str(count))
            if nums[l] ==maxx and count == 1:
                print("OP")
                maxx = float('-inf')
                for i in range(l+1,r):
                    if nums[i] > maxx:
                        maxx = nums[i]
                        count = 1
                    elif nums[i] == maxx:
                        count += 1
            l +=1
            if nums[r] > maxx:
                maxx = nums[r]
                count = 1
            elif nums[r] == maxx:
                count += 1
            
            if nums[l] == maxx and count > 1:
                count -= 1
            res.append(maxx)

            
    return res



print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))