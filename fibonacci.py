# ask the user for how many fibnacci numbers they want 
freq = int(input('How many fibonacci numbers would you like? '))


def fibonacci(freq):
    result = []

    for i in range(freq):
        if i == 0 or i == 1:
            result.append(1)
        else:
            result.append(result[i-1] + result[i-2])

    return result

print(fibonacci(freq))
    
