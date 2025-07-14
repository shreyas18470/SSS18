'''
Created on 12-Jul-2025

@author: Admin
'''
#age=int(input("'please enter your age:"))

'''if age>18:
    print("allow inside")
else:
    print("don't allow"
'''
''' 
if age <=0:
    print("please give valid input")

elif age<13:
    print("you're a child")
elif age>13 and age <= 18:
    print("you're a teenager")
elif age>18 and age <= 60:    
    print("you're a adult")
else:
    print("you are a senior citizen")
'''    
'''
if age <= 0:
    print("please enter valid input")
elif age > 18:
    if age > 60:
        print("you're senior citizen")
    else:
        print(" you are an adult")
else:
    if age<13:
        print("you're a child")
    else:
        print("you're a teenager ")   
    '''
#num=int(input("enter a number"))
'''
if (num%2==0):
    print("even number ")
    
else:
    print('odd number')
 '''   
    
#num=int(input("enter a number"))
'''
if num> 0:
    print("the number is positive")
elif num< 0:
    print("the number is negative")
else:
    print("the number is zero")
    '''
    
#num1=float(input("enter first number"))
'''
num2=float(input("enter second number"))
num3=float(input("enter third number"))
if num1 > num2:
    print(f"the largest number is {num1}")
elif num2 > num1:
    print(f"the largest number is {num2}")
else:
    print("both numbers are equal")
   '''
   
#num1=int(input("the first number"))
'''
num2=int(input("the second number"))
num3=int(input("the third number"))
if num1 >= num2 and num1 >= num3:
    print(f"the largest number is {num1}")
elif num2 >= num1 and num2>= num3:
    print(f"the largest number is {num2}")
else:
    print("the largest number is {num3}")
   '''
   
#age = int(input("enter your age:"))
'''
if age >= 18:
    print("you are eligible")
else: 
    print("you are not eligible") 
'''

#num= int(input("enter a number "))
'''
if num % 11 == 0 and num % 5 == 0:
    print(f"its devisible by both 11 and 5")
else:
    print(f"its not devisible by both 11 and 5")
    '''
    
#if c1=="yes":
'''
    c= float(input("enter the celsius value"))
    result1 = (c*9/5)+32
    print("result1")
if d1 == "yes":
    d= float(input("enter the fahrenheit value"))
    celsius = (f-32)*5/9
    print("celsius")
'''
    

#units = int(input("enter the number of units consumed"))
'''
bill = 0
if units <= 100:
    print(100 * 5)
elif units <= 200:
    print(100 *  + units - 100 * 7)
else:
    print(100 * 5+100 * 7+units - 200*10)
    print(f"electricty bill for {units} units is $ {bill}")
    '''
    
#unit= int(input("enter your age "))
'''
if unit < 5:
    print("free")
elif unit <18:
    print("half fare")
else:
    print("full fare")
    '''
    
#roll= int(input("roll number"))
'''
if roll <20:
    print("third class ")
elif roll <40:
    print("second class")
else:
    print("first class ")
    '''
    
#age= int(input("enter age "))
'''
if age <13:
    print("get the hell out of here you child")
elif age <18:
    print("fucking teenager not allowed ")
elif age <50:
    print("you are welcome")
else:
    print("senior citizen not allowed")
    '''
    
#print('login userid and passward---')
    
    
#correct_username = "shreyas"
'''
correct_passward = "shre1234"

username=input("enter username")
passward=input("enter passward")
if username == correct_username and passward == correct_passward:
    print("login successful")
else:
    print("invalid user id or passward")
 '''
 
# print("atm withdeawal------")
'''
 
balance=int(input("check balance"))
if balance <10000:
    print("allow withdrawal")
else:
    print("insufficient balance")
   '''
#print("blood donating age calculation")
    
#blood=int(input("enter age to donate blood"))
'''
if blood < 18:
    print("can't donate")
elif blood< 50:
    print("can donate")
else:
    print("can't donate")
    '''
    
#student=int(input("enter marks"))
'''
if student <= 90 and <=100:
    print("grade A")
elif student <= 80 marks <=89:
    print("grade B")
elif student <= 70 marks <=79
    print("grade C")
elif student <= 60 marks <=69:
    print("grade D")
else:
    print("grade F")
    '''
    
marks = int(input("Enter the student's marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks <= 89:
    print("Grade: B")
elif marks >= 70 and marks <= 79:
    print("Grade: C")
elif marks >= 60 and marks <= 69:
    print("Grade: D")
elif marks >= 0 and marks < 60:
    print("Grade: F")
else:
    print("Invalid marks")