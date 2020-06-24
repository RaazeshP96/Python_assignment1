'''

Write a Python program to remove an item from a tuple. 

'''
# tuples are immutable, we can not remove  item
# but we can create anpther tuples removing item using slicing

# let tuple1
tuple1 = (1, 2, 3, 4, 5)
tuple1 = tuple1[:-2]  # remove last 2 element
print(tuple1)
