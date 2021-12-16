# L10: https://reurl.cc/bn0kly

def divide(n1 = 10, n2 = 2):
    print(n1/n2)

divide(50, 2)
divide(2, 50)
divide(n2 = 2, n1 = 50)
divide()

print("#########")

def avg(*ns):
    print(ns)
    sum = 0
    for n in ns:
        sum += n
    print(sum/len(ns))

#avg(3, 4)
#avg(3, 5, 10)
avg(1, 4, -1, -8)


