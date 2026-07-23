from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def find_area(self):
        pass
    @abstractmethod
    def find_circumference(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def find_area(self):
        return math.pi * self.radius ** 2
    
    def find_circumference(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def find_area(self):
        return self.length * self.width
    
    def find_circumference(self):
        return 2 * (self.length + self.width)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def find_area(self):
        return self.side ** 2
    
    def find_circumference(self):
        return 4 * self.side
    

# s1 = Shape() # this is an error, because class is an abstract class.
s1 = None

s1 = Circle(1)

print(f"Area of circle: {s1.find_area()}")
print(f"Circumference of circle: {s1.find_circumference()}")

s1 = Rectangle(1, 1)

print(f"Area of rectangle: {s1.find_area()}")
print(f"Circumference of rectangle: {s1.find_circumference()}")

s1 = Square(1)

print(f"Area of square: {s1.find_area()}")
print(f"Circumference of square: {s1.find_circumference()}")

