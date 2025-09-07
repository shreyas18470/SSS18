'''
Created on 22-Jul-2025

@author: Admin
'''
'''
list1 = []
print(list1)
print(type(list1))
'''
'''creation of list with elements'''
'''
list2 = [1, 2, 3, 4,5]
print(list2)
print(type(list2))
'''

'''creation of list using built in function'''
'''
list3 = list(range(10))
print(list3)
print(type(list3))
'''
'''
list4 = ["chocolate, lays, apple, carrot"]
print("list4--->",list4)
print(type(list4))
'''

'''creation of heterogeneous list'''
'''
list5 = [1, 2, 3, 4+5j, "shreyas", True, None]
print("---->", list5)
'''
'''creation of list with duplicate elements'''
'''
list6 = [1,1, 2,2, 3,3, "shreyas","shreyas",True,True, None,None]
print("---->",list6)
'''
'''
list7 = [5,6.3,77,88,3,26,1,2,9,10]
print(list7)
'''
'''accessing using index'''
'''
print("5th element in list5:",list5[5])
print("5th elements in list6:",list6[-5])
'''

'''modification of existing list - add/delete/replace'''
'''
list6[1] = 33
print("list2--->", list6)
'''

#while list6:
   # print(list6)
'''
for i in list5:
    print(i)
'''


'''
print("list--->",list5)
print("list5[2:7]",list[2:7])
print("list5[2:7:2",list5[2:7:2])
print("list5[:7]",list5[:7])
print("list5[2:]",list5[2:])
print("",list6[:5])
print("",list5[1:6])
'''
'''predefined functions'''
'''
print(" ",len(list3))
print(" ",len(list5))
print(" ",len(list6))
del(list5[2])
'''

'''list specific predefined fuctiond'''
'''
list3.append(10)
print("after appending list3 with 15:",list3)
list3.append(list2)
print("after appending list3 with list2:",list3)
'''

#print("count of 3 in list6",list6.count(3))
'''
list2.extend(list3)
print(list2)
'''

'''accessing using slicing operator tuple '''
'''
'''


#print("index of 4 is ",list5.index(3))
#print("index of 4 after 4 is ",list5.index(4, 5))
'''
list5.insert(3,45)
print("list4 after inserting 45 before index 4:",list5)
'''
'''
list5.pop(3)
print("popping element at index 5:",list5)
'''
'''
print("list3.pop()",list5.pop())
print(" ",list5)
'''


'''
list7.sort()
print(" ",list7)
'''

'''create a new list from list2 by multiplying 2 to each element'''
#print7=[]
'''
for i in list2:
    list7.append(i*2)
print("list7:",list7)
'''








list11 = ["apple","banana","mango","chocolate","apple","lays","banana","apple","mango"]
print("my list:",list11)
element = input("choose an element from list:")
count = list11.count(element)
print(count)
print("index is:", list11.index(element))
indices = []
for i in range(len(list11)):
    if list11[i] == element:
        indices.append(i)

print("All indices are:", indices)
choice = input("Enter the index to remove the element (or type 'All' to remove all): ")






