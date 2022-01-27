# take list and remove duplicate elements
# def remove_duplicates(l):
#     unique = []

#     for el in l:
#         if el not in unique:
#             unique.append(el)

#     return unique

def remove_duplicates(l):
    return list(set(l))

print(remove_duplicates([2,4,5,5,6,6,9,10,10,10]))