'''
Write a Python program to sort a list of tuples using Lambda. 

'''

res=lambda tup: sorted(tup)


tup = ('a', 'f', 'b', 'z', 'd', 'c')
print(res(tup))