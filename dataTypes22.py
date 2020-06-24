'''
Write a Python program to remove duplicates from a list. 

'''


def removDub(list1):
    tempSet = set(list1)
    return [i for i in tempSet]


n = int(input("Enter the no of items in list:"))
list1 = []
for i in range(n):
    m = input(f"Enter the {i+1}th item:")
    list1.append(m)
print(removDub(list1))
