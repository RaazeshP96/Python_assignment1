'''
Write a Python function to find the Max of three numbers.

'''


def maxNo(n1, n2, n3):
    return max([n1, n2, n3])


n1 = int(input("enter the 1st no:"))
n2 = int(input("enter the 2nd no:"))
n3 = int(input("enter the 3rd no:"))
print(maxNo(n1, n2, n3))
