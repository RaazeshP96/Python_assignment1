'''
 Write a Python program to sort a list of dictionaries using Lambda. 

'''

res=lambda dic: sorted(dic)

# sample value
dic = {'v': 30, 'd': 60, 'm': 10, 'n': 40, 'f': 50, 'e': 40}
print(res(dic))