'''
    Write a Python program that accepts a comma separated sequence of words
    as input and prints the unique words in sorted form (alphanumerically).

    Sample Words : red,white,black,red,green,black
    Expected Result : black,black,green,red,red,white

'''


def commaSeparated(sentence):
    list1 = sentence.split(',')
    list2 = sorted(list1)
    result = ','.join(list2)
    return result


sentence = input("Enter a comma separated sequence of words: ")
print(commaSeparated(sentence))
