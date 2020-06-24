'''
Write a Python function to create the HTML string with tags around the word(s).

Sample function and result:
    add_tags('i', 'Python') -> '<i>Python</i>'
    add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

'''


def add_tags(tag, word):
    return f" <{tag}>{word}</{tag}> "


tag = input("enter the tag:")
word = input("enter the word:")
print(add_tags(tag, word))
