'''
Created on 03-Aug-2025

@author: Admin
'''
'''
def welcome(name):
    print(f" hi {name}welcome to programming//")
    
welcome("shreyas")


def find_length(ds):
    welcome("shreyas")
    count=0
    for i in ds:
        count+=1
        
   # print(count)
    return count

    
        
find_length([1,2,3,4,5,6])
print(find_length([1,2,3,4,5,6]))
'''




def foo(x):
    x = ['def', 'abc']
    return id(x)
q = ['abc', 'def']
print(id(q) == foo(q))