'''
Created on 26-Jul-2025

@author: Admin


dictionary: we store data in key- value pairs within '{}'

syntax:
      {key1:value1,key2:value2,key3:value3....}
1. empty dictionary can be created
2. dictionary can be created with built in function "dict()" using keywords arguments 

'''
dict1={}
print('dict1',dict1)
print('type of dict1',type(dict1))


dict2={1:"shreyas",2:"tejas",3:"nithin"}
print("dict2",dict2)

dict3=dict(one="shreyas",two="unknown")
print("dict3",dict3)

dict4={"shreyas","shreyas"}#dict wont consider duplicate values
print("dict4",dict4)

dict5={1:"ganashree",2:"kannada kasturi",3:"nithin",4:"vivek"}
print("dict5",dict5)

dict6={1:"ganashree",2:"kannada kasturi",3:"nithin",4:"nithin"}
print("dict6",dict6)

print("------accessing the elements------")
print(dict6[2])

print("-------using for loop--------")
for i in dict6:
    print(i)
    
    
print("-----slicing operator-----")
#print(dict6[1:3])

print("====modification======")
print("dict6 before modification-->",dict6)
dict6[4]="shreyas"
print("dict6 after modification-->",dict6)
dict6[50]="shreyas"
print("dict6 after addition--->",dict6)


dict7=dict6.fromkeys([1.0,2.0,3.0,4.0],"dummy")
print("dict6-->",dict6)
print("dict7--->",dict7)


print("======get()======")
print(dict5.get(4,"key is not present"))
print(dict6.get(5,"key is not present"))


print("=====items=====")
print(dict6.items())

print("====keys=====")
print(dict5.keys())

print("=======values=======")
print(dict5.values())

print("=========iterating over values of a dictionary======")
for i in dict6.values():
    print(i)
    
print("========update======")
dict6.update(dict5)
print("dict after update",dict6)


print("====update from keyword arguments=====")
dict6.update(one="sanjana" ,two="sharina" ,ten="tejas")
print(" ",dict6)


 

        