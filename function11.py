'''

Write a Python program to create a lambda function that adds 15 to a given 
number passed in as an argument, also create a lambda function that multiplies 
argument x with argument y and print the result. 

'''
res1=lambda x:x+15


n=int(input("Enter the integer:"))
print(res1(n))
# =========================================================


res2=lambda x,y: x*y

x=int(input("Enter the 1st integer:"))
y=int(input("Enter the 2nd integer:"))
print(res2(x,y))