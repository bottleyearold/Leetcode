def numSubarrayProductLessThanK(nums, k):
    product = 1
    counter = 0
    l = 0

    for r in range(0, len(nums)):
        product *= nums[r]
        while product >= k and l <= r:
            product = product // nums[l]
            l += 1
        counter += (r-l+1)
    return counter
        


                
print(numSubarrayProductLessThanK(nums = [1,1,1], k = 289))





#     result_list = [1]
#     j = 1
#     val = True
#     store = 1
#     for i in nums:
#         store *= i
#     if store < k:
#         return int((len(nums)*(len(nums)+1))/2)
#     for i in range(0,len(nums)):
#         if nums[i] < k:
#             result_list.append(nums[i])
#             while val:
#                 if result_list[-1]*nums[j] < k:
#                     result_list.append(result_list[-1]*nums[j])
#                     j+=1
#                     if j >= len(nums):
#                         j = i + 2
#                         break
#                 else:
#                     j = i + 2
#                     break
#         else:
#             j = i + 2
        
#         if j >= len(nums):
#             break 
#     if nums[-1] < k:
#         result_list.append(nums[-1])
#     return len(result_list)-1
