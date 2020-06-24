'''
Write a Python program to count the occurrences of each word in a given
sentence.

'''

from collections import Counter


def countWord(sentence):
    list1 = sentence.split(' ')
    print(list1)
    count = Counter(list1)
    dic = dict(count)
    return dic


sentence = input("Enter the sentence:")
print(countWord(sentence))
