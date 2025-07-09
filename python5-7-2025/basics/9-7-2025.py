'''
Created on 09-Jul-2025

@author: Admin
'''
from sys import audit
num1 = 21
num2= 22 + 7j
print(f"sum of {num1} and {num2} is",num1+num2)
print(f"sum of {num2} and {num1} is ",num2+num1)

print("------------------------")
num3 = 45
num4 = 50
print(f" difference of {num3} and {num4} is ",num3-num4)
print(f"difference of {num4} and {num3} is",num4-num3)

print("-------------------------")
num5 = 88
num6 = 78.8
print(f"multi of {num5} and {num6} is ",num5*num6)
print(f"multi of {num6} and {num5} is ",num6*num5)

print("-------------------------")
num7 = 67.6
num8 = 56
print(f'divide of {num7} and {num8} is ',num7/num8)
print(f'divide of {num8} and {num7} is',num8/num7)

print('-------------------------')
print(f"module is {num5} and {num6} is",num5%num6)
print(f"module is {num7} and {num8} is",num7%num8)

print('-------------------------')

print("relationl operators")
print(f"is {num7} greater than {num8}",num7>num8)
print(f"is {num8} greater than{num7}",num8>num7)

print(f"is {num8} greater than{num7}",num8<num7)
print(f"is {num8} greater than{num7}",num8<num7)

print("----logical operations  ")

bool1 = True
bool2 = False

print(f'{bool1} and {bool2}',bool1 and bool2)
print(f'{bool2} and {bool1}',bool2 and bool1)

print('----------or------')
car1 = 'bmw'
car2 = "audi"
print(f"{car1} or {car2}",car1 or car2)
print(f"{car2} or {car1}",car2 or car1)

print("---------not----")
animal1 = 'dog'
animal2 = "cat"

print(f"{animal1} not", not animal1)

print("----------------")
print("is 'S' in 'shreyas",'S' in 'shreyas')
print("is 's' in  'shreyas", 's' in 'shreyas')
print("is 'M' not in  'shreyas", 'M' not in 'shreyas')
print("is 'y' not in 'shreyas", 'y' not in 'shreyas')

num11 = 45
num12 =45.5
print(id(num11))
print(id(num12))

print(f'{num11} and {num12} is identical',num11 is num12)
print(f"{num12} and {num11} is not identical",num12 is not num11 )
