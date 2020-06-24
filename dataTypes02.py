'''
Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.

Sample String : 'restart'
Expected Result : 'resta$t'
'''


def firstOccurance(stringIn):
    result = stringIn[0]
    for i in range(1, len(stringIn)):
        result = result + '$' if stringIn[0] == stringIn[i] else result + stringIn[i]
        # ternary condition operator
    return result


stringIn = input("Enter the string ")
print(firstOccurance(stringIn))
