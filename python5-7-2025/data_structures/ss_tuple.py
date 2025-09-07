'''
Created on 26-Jul-2025

@author: Admin
'''
tuple1 = ()
print(tuple1)

print('=====creation of tuple with elements======')
tuple2 = (1,2,3,4,5)
print("--->",tuple2)
print(type(tuple2))

print("======creation of function using built in function====")
tuple3 = tuple(range(10))
print("--->",tuple3)
print(type(tuple3))



tuple4 = (1,2,3,4,5+7j,"shreyas","shreyas",True,None)
print(tuple4)


print(" ",tuple2[1:4])
print("",tuple4[1:6])


print(" ",len(tuple4))
print(" ",len(tuple3))


tuple2.count 
print(tuple2)

tuple3.count(tuple4)
print(tuple3,tuple4)


tuple2.index
print(tuple2)


print("=========access using index========")
#print(" ",tuple4(5))                                # object is not callable


print('Modification of existing list- Add/delete/replace(re-initialize')
#tuple4(4) = 40
#print("",tuple4)          #cannot assign to function call here. Maybe you meant '==' instead of '='?

print("====slicing operator=====")
tuple8 = (10,20,30,40,50,60,70,80,90)
#print("tuple8 -->", tuple8(5:))         #SyntaxError: invalid syntax
print("tuple8--->", tuple8[1:6])
print("tuple8--->",tuple8[-5:-6:-7])
print("tuple8--->",tuple8[-4:-1])

print("=====predefined functions=====")
print(" ",len(tuple4))
print(" ",len(tuple2))

print("=========specific predefined functions======")
tuple9 = (1,2,2,3,4,5,6,7,2,3,5)
print(tuple9.count(2))



tuple10 = (10,20,30,40,10,20,50)
print(tuple10.index(20,2))



    
a = [1,2,3,4]
for a [-1] in a :
    print(a[-1])
    print(a)
    
