'''

Write a Python program to clone or copy a list. 

'''
import copy


def copyList(l1):
    l2 = copy.deepcopy(l1)
    return l2

# given sample
l1 = [1, 2, 3, 4]
print(copyList(l1))
