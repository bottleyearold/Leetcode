def totalFruit(fruits):
    valid_fruit = []
    list_maxes = []
    difference = 0
    for i in range(0,len(fruits)):
        #if fruit is already in list
        if fruits[i] in valid_fruit: 
            valid_fruit.append(fruits[i])
        else:
            #first instance of new fruit 
            if difference == 0:
                valid_fruit.append(fruits[i])
                difference += 1
            elif difference == 1:
                valid_fruit.append(fruits[i])
                difference += 1
            else:
                #difference greater than 2 and not in fruit 
                list_maxes.append(len(valid_fruit))
                counter = 0
                for j in valid_fruit[::-1]:
                    if j == valid_fruit[-1]:
                        counter += 1
                    else:
                        break
                del valid_fruit[0:len(valid_fruit)-counter]
                valid_fruit.append(fruits[i])
    list_maxes.append(len(valid_fruit))

    return max(list_maxes)






print(totalFruit([1,2,3,2,2]))

# def tester(valid_fruit):
#     counter = 0
#     for j in valid_fruit[::-1]:
#         if j == valid_fruit[-1]:
#             counter += 1
#         else:
#             break
#     del valid_fruit[0:len(valid_fruit)-counter]
#     return valid_fruit
# print(tester([2,3,2,5,3,3]))