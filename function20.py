'''
Write a Python program to find intersection of two given arrays using 
Lambda. 

'''
array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]


intercep=list(filter(lambda x: x in array1, array2)) 
print(intercep)