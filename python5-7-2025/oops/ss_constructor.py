'''
Created on 14-Aug-2025

Constructor:

__init__()--> it is a magic method used to construct an object

magic method --> it is a predefined method which has specific function to do

1. Constructor can be called explicitly like any other method
2. Constructor can be with parameters or without parameters
3. it is not mandatory to define a constructor when a class is defined without a constructor 
python will have its own constructor defined.

diff b/w method and constructor:
method:  
1. method is uesd to define opereations/actions/functions
2. method has to be called explicitly
3. method has to be called explicity
constructor:
1. constructor is used to construct/ initialize an object with specific features
2. Constructor name should always be '__init__'
3. Constructor is called implicitly at the time
 
'''

class shreyasClass():
    def __init__(self, name, roll_no):
        print(f"A new student object {name} is created with roll_no {roll_no}")
        
student1 = shreyasClass("shreyas" ,1)