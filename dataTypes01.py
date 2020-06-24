'''

Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'


Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

'''


# importing Counter class
'''
A Counter is a dict subclass for counting hashable objects. 
It is a collection where elements are stored as dictionary keys and 
their counts are stored as dictionary values.
'''




from collections import Counter
def characterfrequency(stringInput):
    count = dict(Counter(stringInput))
    res = dict(count)  # converting Counter's object to dictionary
    return res


stringInput = input("enter the string")
print(characterfrequency(stringInput))
