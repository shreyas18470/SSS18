'''
Created on 14-Jul-2025

@author: Admin
'''

choice = int(input("""what animal is this:
                 1. dog
                 2. cat"""))
match choice:
    case 1:
        print("its dog")
    case 2:
        print("its cat")
    case _:
        print("please enter 1 or 2")