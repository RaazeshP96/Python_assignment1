'''
    Write a Python function to insert a string in the middle of a string.
    
        Sample function and result :
        insert_sting_middle('[[]]', 'Python') -> [[Python]]
        insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

'''


def strInStr(str1, str2):
    return str1[:len(str1)//2]+str2+str1[len(str1)//2:]


str1 = input("Enter the first string:")
str2 = input("Enter the second string:")
print(strInStr(str1, str2))
