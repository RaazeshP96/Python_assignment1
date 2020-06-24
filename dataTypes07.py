'''
Write a Python function that takes a list of words and returns the length of the
longest one.

'''


def longestOne(list1):
    grt = 0
    result = ''
    for i in list1:
        if grt < len(i):
            grt = len(i)
            result = i
    return f"{result} is longest with length {grt} "


wordsList = []
n = int(input("Enter the number of words that you want to enter:"))
for i in range(n):
    one_word = input(f"Enter {i+1}th word:")
    wordsList.append(one_word)
print(longestOne(wordsList))
