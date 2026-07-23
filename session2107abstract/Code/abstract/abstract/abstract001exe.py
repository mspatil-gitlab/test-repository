#abstraction example

from abc import ABC,abstractmethod
class Animal(ABC):
    pass
@abstractmethod
def sound(self):
    pass

class dog(Animal):
    def sound(self):
        print("Woof")

class cat(Animal):
    def sound(self):
        print("Meow")

d=dog()
c=cat()

d.sound()
c.sound()
