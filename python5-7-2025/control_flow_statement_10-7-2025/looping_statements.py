'''
Created on 14-Jul-2025

@author: Admin
'''
#for i in range(10, 80):
'''
    print(i)
'''
#count=10
'''
while count>0:
    if count == 5:
        continue
    print(count)
    count-=1
'''

#num=5
'''
while num>0:
    print(num)
    num=-1
    if num == 3:
        break
    else:
        print("done")

'''
#num=6
'''
while num<5:
    print(num)
    num+=1
else:
    print("loop completed")
   ''' 
   
#print("-------negative value in range-------------")
'''

for a in range(-10, 10,):
    print(a,end= ' ')
 '''
'''
cities = ("bangalore","mysuru","mangalore","hubballi")
for city in cities:
    if city =="hubballi":
        print(f"found{city}")
        continue
    print(city)
 '''

    
    

#num = (12, 45, 67, 54,100)
'''
for num in num:
    print(num)
    if num==54:
        break
else:
    print("all printed")
'''
'''
print("----else block continue statement ---------")

count = 0

while count <5:
    count += 1
    if count ==3:
        continue
    print("count is :", count)
else:
    print("loop ended")        
 

#print("-----------else block while for loop -------------")
'''
'''
count = 0

while count <5:
    count += 1
    if count == 3:
        break
    print("count is ",count)
else:
    print("loop ended")
 '''
    
#num=0
'''
while num<10:
    num +=1
    if num == 8:
        continue
    print("count is",num)
else:
    print("loop ended")
 '''
#print("----------using else block with for loop break")
'''
for i in range(5):
    print("Number:", i)
    if i == 2:
        break
else:
    print("Loop finished without break.")    
    
    
print("without break")

for i in range(3):
    print("Number:", i)
else:
    print("Loop finished without break.")
'
#num=0
'''
'''
while num <10:
    num +=1
    if num == -5:
        print("count is",num)
else:
    print("loop ended")
'''
'''
#for i in range(1, 6):
'''
'''
     if i % 2 == 0:
         print(i)
         continue
     print("*")
'''

#for j in range(4):
'''
    for i in range (4):# print row of stars
        print("*",end = " ")# print star and keeps the cursor in the same line
    print()# doesent print anything but takes cursor to the next line 
'''

#for s in range (4):# print row of stars
'''
    for i in range(5):
        print("*",end =" ")# print star and keeps the cursor in the same line
        print()# doesent print anything but takes cursor to the next line
   '''     




#for j in range(4):
'''
    for i in range(4):
        print("shreyas",end =" ")
    print()
    
    
#for i in range (1 ,11):
 #   print(i)
    
    
print("-------------------------------")
    
    
#num = 1
'''
#while num<10:
'''
    print(num)
    num+=1
    if num == 3:
        continue
    else:
        print("done")
'''    
    
    
#for a in range(1, 10):
'''
    print(a, end= " ")
'''    
    
    
    
    
#

#for i in range(3):
'''
    for j in range(3):
        print(i+j,end='')
    print() 
 ''' 
  
  
#for i in range(4):
'''
    for j in range(5):
        print(i+j, end='')
    print()
'''
    
    
    
    
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == -1 or j == 0 or j ==-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
        
        
        
        
        
        
        
n = 5  # Size of the square

for i in range(n):
    for j in range(n):
        # Print * on the border; space inside
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to next line



#s = 5
'''
for i in range(s):
    for j in range(s):
        if i == 0 or i == n -1 or j == 0 or j == n -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
 '''   
    
h = 7

for i in range(h):
    for j in range(h):
        if i == 0 or i == h -1 or j == 0 or j== h -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
for i in range(1, 10):
    print(i,end=" ")
    
    
age = int(input("enter your age"))
if age >18:
    print("allow inside")
elif age <18:
    print("dont allow")
else:
    print("enter your correct age")
    
    
    
while num<10:
    print(num)
    if num ==+1:
        continue
else:
    print("ended")
        
        
        
        
        
