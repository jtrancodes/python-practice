# ask user for num and determine if num is prim 
num = int(input('Input a number: '))

def divisors(num):
    result = []

    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)

    return result

def is_prime(num, nums):
    if len(nums) == 2 and nums[1] == num:
        return (f'{num} is a prime number.')
    else: 
        return (f'{num} is not a prime number.')

nums = divisors(num)

print(is_prime(num,nums))

