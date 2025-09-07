'''
Created on 12-Aug-2025

@author: Admin

class ClassName:
    def method_one(self):
        pass
        
        
class --> keyword 
ClassName --> ClassName should be capitalized(first letter should be in upper case, all other letters
are in lower case). if there are multiple words in a ClassName they are separated with space/unders
'''



class shreyasClass:
    def announce_the_creation(self,name):
        print(f"A new student object {name} is created")
        
student1 = shreyasClass() 
student1.announce_the_creation("shreyas")

print(type(student1)) # <class '__main__.shreyasClass'>

print(dir(student1))