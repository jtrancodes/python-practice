# create function that takes in list and prints all elements less than 5
def less_than_5(l):
    for el in l:
        if el < 5: 
            print(el)

less_than_5([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])