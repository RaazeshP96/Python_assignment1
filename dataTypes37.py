'''

Write a Python program to multiply all the values in a dictionary. 

'''


def mulDictItem(dic):
    s = 1
    for v in dic.values():
        if type(v) is int:
            s *= v
    return s


dic = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
print(mulDictItem(dic))
