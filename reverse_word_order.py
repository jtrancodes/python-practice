# ask user for string and print the string in reverse
string = input('Please input a string that is at least 4 words long: ')

words = string.split()

if len(words) < 4:
    print('Please enter a longer string.')

print(' '.join(words[::-1]))

    

    