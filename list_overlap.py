import random 

# take two lists and return list that has common elements between the lists (no duplicates)

# need a loop to iterate
# intialize empty list to hold the common elements
# if element in list 1 and is in list 2 but NOT in result list, add to result list

list1 = [random.randint(1,20) for i in range(10)]
list2 = [random.randint(1,20) for i in range(10)]

list1.sort()
list2.sort()

print(list1)
print(list2)

def common_integers(l1, l2):
    result = list(set([el for el in l1 if el in l2]))

    # for i in l1:
    #     if i in l2 and i not in result:
    #         result.append(i)
    
    return result


print(common_integers(list1, list2))