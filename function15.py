'''

Write a Python program to filter a list of integers using Lambda. 

'''
# sample data
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# return only even item in the list
print(list(filter(lambda x: (x % 2 == 0), lis)))
