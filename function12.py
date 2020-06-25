'''

Write a Python program to create a function that takes one argument, and 
that argument will be multiplied with an unknown given number.

'''


def multi(n):
    a = int(input("Enter the number:"))
    return f"The required result is { n * a }"


n = int(input("Enter the integer:"))
print(multi(n))
