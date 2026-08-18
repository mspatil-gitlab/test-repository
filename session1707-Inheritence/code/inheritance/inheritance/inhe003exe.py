#Using Super() in inheritance

class Parent:
    def __init__(self,name="Mithun"):
        self.name = name

        print("Parent constructor called")

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
        print("Child constructor called")
    
k1 =Parent()
c1 = Child(21)
print(k1.name)


print(c1.age)

print(c1)
        