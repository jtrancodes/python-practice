# ask user for number and then print out all divisors of that number 
num = int(input('Input a number: '))
result = []

# loop over a range of that number + 1 (so you can include num) and print out all nums that have a remainder of 0
for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)

print(result)
    