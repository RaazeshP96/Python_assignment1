'''

Write a Python script to check whether a given key already exists in a 
dictionary. 

'''


def keyExistance(dict1, key):
    for i in dict1.keys():
        if i == key:
            return f"{key} is already in dictionary"
    return f"{key} is not in dictionary"


# sample test
dict1 = {'a': 1, 'b': 2, 'c': 3}
key1 = 'a'
key2 = 'z'
print(keyExistance(dict1, key1))
print(keyExistance(dict1, key2))
