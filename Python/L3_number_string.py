# L2: https://reurl.cc/82KGod

x1 = 7/6
x2 = 7//6
x3 = 2**3
x4 = 2**0.5
x5 = 7%3

print("integer division = {}\n double division = {}\n square = {}\n root = {}\n mod = {}".format(x1, x2, x3, x4, x5))

print("###########################")

# \ escape
# """ can add next line

print("new line:")
s1 = """Hello


world
"""

s2 = "ABC" "DEF"
print(s1)
print(s2)

print("###########################")

myString1 = "Hel\"lo"
print(myString1)
myString2 = "Hello"
myString3 = "World"



'''
index  0 1 2 3 4 
       W o r l d
'''

print("index access:")
print(myString3[1:4])
print(myString3[1:])
print(myString3[:3])

print("###########################")

print("concatenate string:")
print(myString2 + myString3)
print("Hello "*5 + "World")

