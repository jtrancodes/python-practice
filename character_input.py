from datetime import date

# create input that asks for users name and age
name = input('What is your name? ')
age = int(input('How old are you? '))

# print out message that tells the user the year that they will turn 100
years_until_100 = date.today().year - age + 100

print(f'{name} will turn 100 in the year {years_until_100}.') 