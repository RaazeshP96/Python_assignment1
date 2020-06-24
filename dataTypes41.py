'''

Write a Python program to convert a tuple to a string. 

'''


def tupTostr(tup):
    st = ''
    for i in tup:
        st += str(i)
    return st


# sample tuple
tup = (1, '2', 3, 4, '5')
print(tupTostr(tup))
