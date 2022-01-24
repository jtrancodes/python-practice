# ask the user for a num
num = int(input('Input a number: '))

# print appropriate message depending on if the num is even or odd
if num % 2 == 0:
    print(f'{num} is an even number!')
else:
    print(f'{num} is an odd number!')