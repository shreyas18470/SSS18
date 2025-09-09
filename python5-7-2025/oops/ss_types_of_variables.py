'''
Created on 08-Sept-2025

1. types of variables
2. instance variables (object level variables)
3. static variables (class level variables)
4. global variables

'''
city = "mysuru"
class shreyasClass():
    school_name = "iQuset"
    def __init__(self, name, roll_no):
        print(f"A new student from ,{city} {name} is enrolled for {shreyasClass.school_name}, with roll_no {roll_no}")
        self.name = name
        self.roll_no = roll_no
        shreyasClass.school_name = "iQuest"
    def calculate_percentage(self,kan,eng,sci):
        per=((kan+eng+sci)/300)*100
        print(f"pass percentage {self.name} is: {per}%")
        
obj1 = shreyasClass("shreyas", 100)
obj1.calculate_percentage(100,50,75)
obj1.calculate_percentage(100,20,80)

obj2 = shreyasClass("sansri",200)
obj2.calculate_percentage(100, 70, 55)