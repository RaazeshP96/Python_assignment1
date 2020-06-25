'''
Write a Python function to calculate the factorial of a number (a non-negative 
integer). The function accepts the number as an argument. 

'''


def fact(n):
    f = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            f = f*i
        return f


n = int(input("enter the positive integer:"))
fac = fact(n)
print(f"The factorial of {n} is {fac}")
