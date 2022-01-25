def common_elements(l1,l2):
    return list(set([el for el in l1 if el in l2]))

print(common_elements([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))