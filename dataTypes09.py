'''
Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.

'''


def exchange(str1):
    return str1[-1] + str1[1:-1] + str1[0]


str1 = input("Enter the string:")
print(exchange(str1))
