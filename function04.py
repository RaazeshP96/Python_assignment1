'''

Write a Python program to reverse a string. 
Sample String : "1234abcd" 
Expected Output : "dcba4321" 

'''


def revStr(str1):
    return str1[-1::-1]


str1 = "1234abcd"
print(revStr(str1))
