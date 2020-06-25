'''
Write a Python program to sum all the values in a dictionary.

'''


def sumDictItem(dic):
    s = 0
    for v in dic.values():
        if type(v) is int:
            s += v
    return s


dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sumDictItem(dic))
