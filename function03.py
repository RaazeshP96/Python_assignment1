'''
Write a Python function to multiply all the numbers in a list. 
Sample List : [8, 2, 3, -1, 7]
Expected Output : -336 

'''
import math


def mulList(lis):
    return math.prod(lis)


lis = [8, 2, 3, -1, 7]
print(mulList(lis))
