'''
created on 2-aug-2025

singleline string:
   single double quotes
   single single quotes
   

'''

string3='my name is "vivek"'
print("string3:",string3)


print("len string3:",len(string3))
print("string3[3]:",string3[1])

string4=string3.capitalize()
print("string3 after capitalize:",string4)

string5=string3.casefold()
print("string after casefold:",string5)

string6=string3.center(38, "=")
print("string3 after centering",string6)

print(string3.endswith('"vivek"'))

print(string3.find("v"))
print(string3.find("x"))

print(string3.index("v"))
#print(string3.index("x"))

print(string3.isalnum())
print(string3.isalpha())

string7= "//".join(["today","is","saturday"])
print("string7:",string7)

print(string3.split(" "))
print(string3.split(" ",2))

print(string6.rstrip("="))
print(string6.lstrip("="))


print(string3.partition("is"))

print(string3.rpartition(" "))

string8='my\n name is\n "vivek" '
print("string8:",string8)

print(string3.title())



