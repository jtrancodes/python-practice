# ask user for string 
# print whether the input is a palindrome or not

str = input('Input text to see if it is a palindrome: ')

# print(str[0:])
# print(str[::-1])
# print(str[::])

# if str[0:] == str[::-1]:
#     print('This string is a palindrome')
# else:
#     print('This string is not a palindrome')

def palindrome(str):
    for i in range(len(str)):
        if str[i] == str[-i-1]:
            continue
        else: 
            return 'This string is not a palindrome'
        

    return 'This string is a palindrome.'



print(palindrome(str))