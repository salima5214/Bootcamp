# L18: https://reurl.cc/ZjD00g


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print( self.x, self.y )

    def distance(self, targetX, targetY):
        return (((self.x - targetX)**2) + ((self.y - targetY)**2))**0.5
        
p = Point(3, 4)
p.show()

result = p.distance(0, 0)
print( result )

class File:
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()

f1 = File("L18_data1.txt")
f1.open()
data = f1.read()
print(data)

f2 = File("L18_data2.txt")
f2.open()
data = f2.read()
print(data)