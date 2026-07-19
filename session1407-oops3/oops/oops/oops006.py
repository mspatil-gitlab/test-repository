class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p):
        return Point(self.x + p.x, self.y + p.y)    

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(4, 7)
p2 = Point(5, 11)

print(p1)
print(p2)

p3 = p1.add(p2)

print(p3)




        