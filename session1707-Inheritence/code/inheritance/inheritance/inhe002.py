# single inheritance

class Animal:
    def sound(self):
        return "Animal makes sound."

class Dog(Animal):
    def sound(self): # method overriding
        return "Dog barks."

a = Animal()
print(a.sound())

d = Dog()
print(d.sound())


