'''

Write a Python function that takes a number as a parameter and check the 
number is prime or not. 
Note : A prime number (or a prime) is a natural number greater than 1 and that 
has no positive divisors other than 1 and itself. 

'''


def prime(num):
    d = 0
    for i in range(1, num+1):
        if num % i == 0:
            d += 1
    return f'{num} is prime' if d == 2 else f'{num} is not prime'


num = int(input("Enter the positive integer :"))
print(prime(num))
