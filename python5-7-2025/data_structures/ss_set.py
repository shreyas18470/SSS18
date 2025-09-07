'''
Created on 26-Jul-2025

@author: Admin
'''
set1 = {}
print(set1)


set2 = {1,2,3,4,5,5}
print(set2)


set3 = {1,2,3,4,5,"shreyas",True,5+9j,}
print(set3)

print("======duplicate elements======")
set4 = {1,1,2,2,3,3,4,4,5,5,"shreyas","shreyas",5+6j,5+6j,True,True}
print(set4)


set5 = {10,20,30}
set5.clear()
print(set5)

print("=====using for loop=====")
for i in set4:
    print(i)



print("=====specified predefined functions======")
set7 = {1,2,3,4}
set7.add(6)
print(set7)

set7 = {1,2,3,4}
set7.remove(4)
print(set7)


set8 = {1,2,3}
set8.clear()
print(set8)



