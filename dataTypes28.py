'''
Write a Python script to add a key to a dictionary. 

Sample Dictionary : {0: 10, 1: 20} 
Expected Result : {0: 10, 1: 20, 2: 30} 

'''


def dicAdd(dict1, key, value):
    dict1[key] = value
    return dict1


# As sample above
dict1 = {0: 10, 1: 20}
key = 2
value = 30
print(dicAdd(dict1, key, value))
