def minSubArrayLen(target, nums):
    l = 0
    result = []
    sum = 0
    for r in range(len(nums)):
        sum += nums[r]
        while target <= sum and l <= r:
            sum -= nums[l]
            result.append(r-l+1)
            l += 1
    if result == []:
        return 0
    return min(result)

print(minSubArrayLen(11,[1,1,1,1,1,1,1,1]))