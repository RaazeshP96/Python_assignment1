'''
 Write a Python program to check a list is empty or not.

 '''


def emptyOrNot(list1):
    if list1:
        return "list is not Empty"
    else:
        return "list is empty"


list1 = []
print(emptyOrNot(list1))
list1 = [1, 2, 3]
print(emptyOrNot(list1))
