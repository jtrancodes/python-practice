import string
import random 

def generate_pass():

    password = ''

    for i in range(4):
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)

    return password
    
while True:
    answer = input('Would you like a new password? (Y/N) ')

    if answer == 'N':
        break

    print(generate_pass())

    



