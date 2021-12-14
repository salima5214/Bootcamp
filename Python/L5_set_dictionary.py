# L5: https://reurl.cc/Rbp1WG

s1 = {3, 4, 5}
print(3 in s1)
print(3 not in s1)
print(6 not in s1)

s2 = {4, 5, 6, 7}
s3 = s1 & s2 # intersection
s4 = s1 | s2 # union
print(s3)
print(s4)
print(s1 - s2)
print(s1 ^ s2) # Anti-intersection
print("###################") 
s = set("Hello")
print(s)
print("H" in s)
print("h" in s)
print("a" not in s)
print("###################") 

dic = {"apple": 29, "orange": 19}
print(dic)
dic["apple"] = 35
print(dic)

print("apple" in dic)
print("banana" not in dic)
del dic["apple"]
print(dic)
print("###################") 
dic = {x:x*2 for x in [3, 4, 5]}
print(dic)