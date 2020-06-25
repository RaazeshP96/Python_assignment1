'''

Write a Python program to check whether a given string is number or not 
using Lambda. 

'''


notNum=lambda x: x.isdigit()

str1=(input("Enter the string:"))
print("The given string is number") if notNum(str1) else print("The given string is not number")