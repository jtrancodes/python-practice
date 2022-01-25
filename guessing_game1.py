import random 

winning_num = random.randint(1,9)

user_num = int(input('Choose a number from 1 to 9: '))

print(winning_num)

if user_num > winning_num:
    print(f'Your guess {user_num} is too high.')
elif user_num < winning_num:
    print(f'Your guess {user_num} is too low.')
else:
    print(f'Your guess {user_num} is correct!')
