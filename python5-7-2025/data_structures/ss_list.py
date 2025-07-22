'''
Created on 22-Jul-2025

@author: Admin
'''

list1 = []
print(list1)
print(type(list1))

'''creation of list with elements'''
list2 = [1, 2, 3, 4]
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

tuple2 = (1,2,3,4,5)
print("--->",tuple2)
print(type(tuple2))


tuple3 = tuple(range(10))
print("--->",tuple3)
print(type(tuple3))


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


