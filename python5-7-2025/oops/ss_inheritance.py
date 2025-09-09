'''
Created on 08-Sept-2025

inheritance


Types
'''
class Grandparent:
    def gp_method(self):
        print("this is gp method")
        
        
class Father(Grandparent) :
    def f_method(self):
        print("this is father method")
        
    def car(self):
        print("this is fathers car ")
        
class Mother:
    def m_method(self):
         print("this is mother method")
         
    def car(self):
         print("this is mothers car")

class Child(Father,Mother):
    def c_method(self):
        print("this is child method")
        
print("=======Grandparent method=====")
ajji = Grandparent()
ajji.gp_method()
print("=======father class======")
appa = Father()
appa.f_method()
appa.gp_method()
print("=========child class=======")
nanu = Child()
nanu.c_method()
nanu.f_method()
nanu.gp_method()
nanu.m_method()
nanu.car()

print("=====for child class object====")
print(Child.mro())



