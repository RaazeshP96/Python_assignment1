'''
Write a Python program to get the largest number from a list. 

'''


def lgrList(list1):
    return max(list1)


n = int(input("Enter the no of items in list:"))
list1 = []
for i in range(n):
    m = int(input(f"Enter the {i+1}th integer:"))
    list1.append(m)
print(lgrList(list1))
