'''
Write a Python program to remove the nth
index character from a nonemptystring.

'''


def nthRemove(str1, n):
    return str1[:n] + str1[n+1:]


str1 = input("Enter the nonemptystring:")
n = int(input("enter the nth index: "))
print(nthRemove(str1, n))
