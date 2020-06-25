'''

Write a Python program to remove a key from a dictionary.

'''


def remDictItem(dic, key):
    dic.pop(key)
    return(dic)


dic = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60}
key = input("Enter the key you wanna remove:")
print(remDictItem(dic, key))
