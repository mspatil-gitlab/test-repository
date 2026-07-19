#Create a class Person with the attributes name and age.
#  Create a method update_age() to update the age of the person.
#  Then, create an object of the class, print the initial attributes, 
#  update the age, and print again.

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def update_age(self,age):
#         self.age=age

#     def __str__(self):
#         return f"{self.name} {self.age}"
    
# p1=Person("John",30)
# print(p1.name)
# print(p1.age)
# print(p1)
# p1.update_age(31)
# print(p1)



class person():
    def __init__(self,name="mithun",age=31):
        self.name=name
        self.age=age
        
    def updateage(self,age):
        self.age=age

    def __str__(self):
        return f"{self.name} {self.age}"

p1=person()
print(p1.name,p1.age)
# print(p1.age)
# print(p1)
p1.updateage(21)
# pyrefly: ignore [attr-defined]
print(f"New age:{p1.name} {p1.age}")
