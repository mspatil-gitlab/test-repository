# Multiple Inheritance
class Engine:
    def start(self):
        return "Engine starts"

class Wheels:
    def rotate(self):
        return "Wheels rotate"

class Car(Engine, Wheels):  # Car inherits from both Engine and Wheels
    def drive(self):
        return "Car is moving"

c = Car()
print(c.start())   # Output: Engine starts
print(c.rotate())  # Output: Wheels rotate
print(c.drive())   # Output: Car is moving
