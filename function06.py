'''

Write a Python function to check whether a number is in a given range.

'''


def checkRange(a, f, n):
    return True if a in range(f, n+1) else False


a = int(input("Enter a number:"))
f = int(input("Enter 1st term in range:"))
n = int(input("Enter nth term in range:"))
print(checkRange(a, f, n))
