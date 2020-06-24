'''
Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given list of 
strings. 

Sample List : ['abc', 'xyz', 'aba', '1221'] 
Expected Result : 2 


'''


def strList(list1):
    s = 0
    for i in list1:
        if len(i) >= 2 and i[:1] == i[-1:]:
            s = s+1
    return s


n = int(input("Enter the no of items in list:"))
list1 = []
for i in range(n):
    m = input(f"Enter the {i+1}th string:")
    list1.append(m)
print(strList(list1))
