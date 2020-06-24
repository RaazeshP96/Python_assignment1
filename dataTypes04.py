'''
Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

'''


def singleString(str1, str2):
    result1 = str2[:2]+str1[2:]
    result2 = str1[:2]+str2[2:]
    return f"{result1} {result2}"


str1 = input("Enter the first string ")
str2 = input("Enter the second string ")
print(singleString(str1, str2))
