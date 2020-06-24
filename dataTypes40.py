'''

Write a Python program to add an item in a tuple. 

'''

# tuples are immutable, we can not add  elements
# but we can merge two tuples creating new tuple

# let tuple1
tuple1 = (1, 2, 3, 4, 5)
tuple1 = tuple1+(6,)
print(tuple1)
