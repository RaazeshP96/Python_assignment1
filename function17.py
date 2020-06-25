'''

Write a Python program to find if a given string starts with a given character 
using Lambda. 

'''


firstChar=lambda str1: str1[:1]

str1=input("Enter the string:")
print(firstChar(str1))