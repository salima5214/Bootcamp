# L8: https://reurl.cc/n5eE08

n = int(input("type an integer: "))
for i in range(n):
    if i * i == n:
        print("root = ", i)
        break
else:
    print("no integer of root")

print("###################")

sum = 0
for n in range(11):
    sum += n
else:
    print(sum)

print("###################")

n = 0
while n < 7:
    if n == 3:
        n += 1
        continue
    print(n)
    n += 1

print("###################")

n = 0
while n < 7:
    if n == 3:
        n += 1
        break
    print(n)
    n += 1


