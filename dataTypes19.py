'''

Write a Python program to get the smallest number from a list. 

'''


def smrList(list1):
    return min(list1)


n = int(input("Enter the no of items in list:"))
list1 = []
for i in range(n):
    m = int(input(f"Enter the {i+1}th integer:"))
    list1.append(m)
print(smrList(list1))
