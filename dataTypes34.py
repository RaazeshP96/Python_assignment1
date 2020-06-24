'''

Write a Python script to merge two Python dictionaries. 

'''


def mergeDict(dic1, dic2):
    dic1.update(dic2)
    return dic1


# sample values
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}

print(mergeDict(dic1, dic2))
