'''
     Write a Python program to sum all the items in a list. 

'''


def sumList(list1):
    return sum(list1)


n = int(input("Enter the no of items in list:"))
list1 = []
for i in range(n):
    m = int(input(f"Enter the {i+1}th integer:"))
    list1.append(m)
print(sumList(list1))
