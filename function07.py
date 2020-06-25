'''

Write a Python function that accepts a string and calculate the number of 
upper case letters and lower case letters. 

Sample String : 'The quick Brow Fox' 

Expected Output : 
    No. of Upper case characters : 3 
    No. of Lower case Characters : 12 

'''


def lowerUpper(str1):
    l1 = str1.split(' ')
    str1 = ''.join(l1)
    l = u = 0
    for i in str1:
        if i.isupper():
            u += 1
        else:
            l += 1
    return u, l


str1 = input("Enter the string:")
u, l = lowerUpper(str1)
print(f'No. of Upper case characters :{u}')
print(f'No. of lower case characters :{l}')
