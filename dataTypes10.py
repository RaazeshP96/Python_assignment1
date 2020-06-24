'''
Write a Python program to remove the characters which have odd index
values of a given string.

'''


def removeOdd(str1):
    return str1[::2]


str1 = input("Enter the  string:")
print(removeOdd(str1))
