'''

Write a Python program to square and cube every number in a given list of 
integers using Lambda. 


'''


sq=lambda x:x*x
cub=lambda x:x*x*x

n=int(input("Enter the integer:"))
print(f"Square -> {sq(n)}")
print(f"Cube -> {cub(n)}")