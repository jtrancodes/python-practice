# ask the user for a num
num = int(input('Input a number: '))

# print appropriate message depending on if the num is even or odd
# if num % 4 == 0:
#     print(f'{num} is a multiple of 4!')
# elif num % 2 == 0:
#     print(f'{num} is an even number!')
# else:
#     print(f'{num} is an odd number!')

# EXTRA
check = int(input('Provide another number: '))

if num % check == 0:
    print(f'{check} divides evenly into {num}.')
else: 
    print(f'{check} does not divide evenly into {num}.')
