import random 
guesses = 0

while True:
    winning_num = random.randint(1,9)
    user_answer = input('Choose a number from 1 to 9 or Type exit to leave game. ')

    if user_answer == 'exit':
        break

    user_num = int(user_answer)

    if user_num > winning_num:
        print(f'Your guess {user_num} is too high.')
    elif user_num < winning_num:
        print(f'Your guess {user_num} is too low.')
    else:
        print(f'Your guess {user_num} is correct!')
        guesses += 1
        break

    guesses += 1

print(f'You guessed {guesses} times.')
