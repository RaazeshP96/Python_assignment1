'''
Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.


Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'

'''


def addingIng(str1):
    if len(str1) < 3:
        return str1
    else:
        return str1+'ly' if str1[-3:] == 'ing' else str1+'ing'


str1 = input("enter the string ")
print(addingIng(str1))
