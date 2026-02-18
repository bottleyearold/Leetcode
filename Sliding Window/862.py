#pop + popleft + dequeued_value

def shortestSubarray(nums, k):
    from collections import deque
    d = deque(nums)
    i = 0
    sum = 0 
    count_size = []
    count = 0
    bot = 0
    while d:
        sum += d[i]
        count += 1
        print("sum: " +str(sum))
        while sum >= k and d:
            print("sum: " +str(sum))
            print("VIPPP")
            count_size.append(count)
            count -= 1
            dequeued_value = d.popleft()
            sum -= dequeued_value
            i = 0
            bot = 1
            print(d)
            print("count size: " +str(count_size))
        i += 1
        if bot == 1:
            sum = 0
            bot = 0
            count = 0
            i = 0
        if i == len(d) and sum < k:
            break
        print("sum: " +str(sum))
        print("count:  " +str(count))
        print(d)
        print("count size: " +str(count_size))
        print("i:  " + str(i))
    if count_size == []:
        return -1
    return min(count_size)
            




print(shortestSubarray([84,-37,32,40,95],167))