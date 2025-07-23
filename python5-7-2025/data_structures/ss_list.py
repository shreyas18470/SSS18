'''
Created on 22-Jul-2025

@author: Admin
'''

list1 = []
print(list1)
print(type(list1))

'''creation of list with elements'''
list2 = [1, 2, 3, 4,5]
print(list2)
print(type(list2))


'''creation of list using built in function'''
list3 = list(range(10))
print(list3)
print(type(list3))

list4 = ["chocolate, lays, apple, carrot"]
print("list4--->",list4)
print(type(list4))


'''creation of heterogeneous list'''
list5 = [1, 2, 3, 4+5j, "shreyas", True, None]
print("---->", list5)

'''creation of list with duplicate elements'''
list6 = [1,1, 2,2, 3,3, "shreyas","shreyas",True,True, None,None]
print("---->",list6)


'''accessing using index'''

print("5th element in list5:",list5[5])
print("5th elements in list6:",list6[-5])


'''modification of existing list - add/delete/replace'''

list6[1] = 33
print("list2--->", list6)


#while list6:
   # print(list6)
    
    
for i in list5:
    print(i)




tuple1 = ()
print(tuple1)

'''creation of tuple with elements'''

tuple2 = (1,2,3,4,5)
print("--->",tuple2)
print(type(tuple2))

'''creation of list using built in function'''

tuple3 = tuple(range(10))
print("--->",tuple3)
print(type(tuple3))

'''creation of heterogeneous list'''

tuple4 = (1,2,3,4,5+7j,"shreyas","shreyas",True,None)
print(tuple4)

#print("4th element in tuple4",tuple4(4))


set1 = {}
print(set1)


set2 = {1,2,3,4,5,5}
print(set2)


set3 = {1,2,3,4,5,"shreyas",True,5+9j,}
print(set3)


set4 = {1,1,2,2,3,3,4,4,5,5,"shreyas","shreyas",5+6j,5+6j,True,True}
print(set4)


'''accessing using slicing operator'''
print("list--->",list5)
print("list5[2:7]",list[2:7])
print("list5[2:7:2",list5[2:7:2])
print("list5[:7]",list5[:7])
print("list5[2:]",list5[2:])
print("",list6[:5])
print("",list5[1:6])
'''predefined functions'''

print(" ",len(list3))
print(" ",len(list5))
print(" ",len(list6))
del(list5[2])


'''list specific predefined fuctiond'''
list3.append(10)
print("after appending list3 with 15:",list3)
list3.append(list2)
print("after appending list3 with list2:",list3)


print("count of 3 in list6",list6.count(3))

list2.extend(list3)
print(list2)


'''accessing using slicing operator tuple '''

print(" ",tuple2[1:4])
print("",tuple4[1:6])

'''predefined functions'''


print(" ",len(tuple4))
print(" ",len(tuple3))

tuple2.count 
print(tuple2)

tuple3.count(tuple4)
print(tuple3,tuple4)

tuple2.index
print(tuple2)

print(" ",len(set2))