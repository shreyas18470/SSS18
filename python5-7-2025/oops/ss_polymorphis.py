'''
Created on 10-Sept-2025

polymorphism: anything which appears in many forms 

poly = many
morph = forms

'+' sign --> addition,list extension,string concatenation
'+' sign --> 

types of polymorphism:
1. overloading:
     a. operator overloading :an operator performs different operations based on the types of operands based on the types of operands 
     b. method overloading : more than one method having same name but with different no./types of arguments
     c. constructor overloading : a class having more than one constructor with different no./types of arguments
     
     - both in method overloading and constructor overloading a particular method / constructor is called
     based on no./ types of arguments passed 
     - but in python strict method overloading/constructor overloading and constructor overloading 
     
2. overriding:
     a. method overriding 
     b. constructor overriding
'''
from typing import overload

class Example:
#    @overload
    def method1(self, a=0,b=0,c=0):
        print(f"method1 with {self.num}  parameters")
        
    def method1(self, num1, num2):
        print(f"method1 with {num1} parameter")
        
        
ex1 = Example()
#ex1.add_infinite()
#ex1.add()