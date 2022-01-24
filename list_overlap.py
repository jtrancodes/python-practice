# take two lists and return list that has common elements between the lists (no duplicates)

# need a loop to iterate
# intialize empty list to hold the common elements
# if element in list 1 and is in list 2 but NOT in result list, add to result list

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common_integers(l1, l2):
    result = []

    for i in l1:
        if i in l2 and i not in result:
            result.append(i)
    
    return result


print(common_integers(list1, list2))