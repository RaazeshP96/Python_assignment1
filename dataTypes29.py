'''
Write a Python script to concatenate following dictionaries to create a new 
one. 

Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60} 
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

'''
import copy


def mergeDict(dic1, dic2, dic3):
    result = copy.deepcopy(dic1)
    result.update(dic2)
    result.update(dic3)
    return result


# given sample
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


print(mergeDict(dic1, dic2, dic3))
