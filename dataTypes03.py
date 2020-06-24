'''
Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String

'''


def first2Last2(stringInput):
    length = len(stringInput)
    if length < 2:
        result = "Empty String"
    else:
        first2 = stringInput[:2]
        before = length-2
        last2 = stringInput[before:]
        result = first2+last2
    return result


stringInput = input("enter the string ")
print(first2Last2(stringInput))
