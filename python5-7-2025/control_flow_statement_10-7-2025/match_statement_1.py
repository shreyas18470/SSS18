'''
Created on 14-Jul-2025

@author: Admin
'''

#choice = int(input("""what animal is this:
'''
                 1. dog
                 2. cat"""))
               
match choice:
    case 1:
        print("its dog")
    case 2:
        print("its cat")
    case _:
        print("please enter 1 or 2")
'''
    
    
fruit = ""

match fruit:
    case "apple":
        print("its apple")
    case "banana":
        print("its banana")
    case "mange":
        print("its mango")
    case _:
        print("un known fruit")
        
        
        
car = "rr"
match car:
    case "suzuki":
        print("its suzuki")
    case "audi":
        print("its audi")
    case "tesla":
        print("its tesla")
    case _:
        print("what the fuck is this car")
        
        
