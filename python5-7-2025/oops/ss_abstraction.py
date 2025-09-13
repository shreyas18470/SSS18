'''
Created on 13-Sept-2025

Abstraction: some thing existing in thought as an idea but not having a physical or concrete

if a feature / method differs in its implementation in different /sub classes we just define 
unimplemented method in parent /super class and declare it as abstract method .

thus ,any class having one or more abstract method is called as abstract class.

from an abstract class object can't be created (an abstract class can't be instantiated)

So it makes mandatory for child classes to provide implementation for an abstract method.
'''
from abc import abstractmethod


class car:
    def move_forward(self):
        print("car is moving forward")
        
    @abstractmethod
        
    def drive_train(self):
        pass
    
class hatch_back(car):
    def move_backward(self):
        print("car is moving backward ")
        
    def drive_train(self):
        print("front wheel drive is implemented")
    
        
swift=hatch_back()
swift.move_forward()
swift.drive_train()    
