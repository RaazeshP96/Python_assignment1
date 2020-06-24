'''

Write a Python program to find the first appearance of 
the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.



Sample String : 'The lyrics is not that poor !'
'The lyrics is poor !'

Expected Result : 'The lyrics is good !'
'The lyrics is poor !'

'''


def notPoor(st1):
    list1 = st1.split(' ')
    posNot = 0
    posPoor = 0
    if "poor" in list1 and "poor" in list1:
        posNot = list1.index("not")
        posPoor = list1.index('poor')
    if posNot < posPoor:
        newList = list1[:posNot]
        newList.append('good')
        fnlList = newList+list1[posPoor + 1:]
        result = ' '.join(fnlList)
    else:
        result = ' '.join(st1)
    return result


st1 = input("enter the string ")
print(notPoor(st1))
