'''
Write a Python program to insert a given string at the beginning of all items in 
a list. 

Sample list : [1,2,3,4], string : emp 
Expected output : ['emp1', 'emp2', 'emp3', 'emp4'] 

'''


def insertFirst(item, list1):
    return [item + str(i) for i in list1]


list1 = [1, 2, 3, 4]  # just assuming the list
item = input("Enter the string:")
print(insertFirst(item, list1))
