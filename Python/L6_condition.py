# L6: https://reurl.cc/95jXlV

x = input("Type a number: ")
x = int(x)

if x > 90:
    print("Excellent")
elif x > 60:
    print("PASS")
else:
    print("FAIL")

print("##################")

n1 = int(input("number 1: "))
n2 = int(input("number 2: "))
op = input("type + - / *: ")

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
else:
    print("not support")