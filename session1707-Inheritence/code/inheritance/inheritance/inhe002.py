# single inheritance

class Animal:
    def sound(self):
        return "Animal makes sound."

class Dog(Animal):
    def sound(self): # method overriding
        return "Dog barks."
class Cat(Animal):
    def sound(self):
        return "Cat meow"

# a = Animal()
# print(a.sound())

# d = Dog()
# print(d.sound())

# c = Cat()
# print(c.sound())

animals = [Animal(),Dog(),Cat()]
for a in animals:
    print(a.sound())
 


