'''
Write a Python program to multiplies all the items in a list. 

'''
import math


def mulList(list1):
    return math.prod(list1)


n = int(input("Enter the no of items in list:"))
list1 = []
for i in range(n):
    m = int(input(f"Enter the {i+1}th integer:"))
    list1.append(m)
print(mulList(list1))
