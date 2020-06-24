'''

Write a Python program to check whether all dictionaries in a list are empty or 
not. 
Sample list : [{},{},{}] 
Return value : True 

Sample list : [{1,2},{},{}] 
Return value : False 

'''


def dictEmpty(list1):
    for i in list1:
        if i:
            return False
        else:
            return True


l1 = [{}, {}, {}]
l2 = [{1, 2}, {}, {}]
print(dictEmpty(l1))
print(dictEmpty(l2))
