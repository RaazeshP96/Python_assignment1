'''
Write a Python program to replace the last element in a list with another list. 

Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8] 
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8] 

'''


def replaceLast(list1, list2):
    list1.pop()
    list1.extend(list2)
    return list1


list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
print(replaceLast(list1, list2))
