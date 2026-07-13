class student:
    def __init__(self,name,age,course):
        self.name =name
        self.age = age
        self.course = course

    def __str__(self):
        return(f"Name {self.name} age :{self.age} course:{self.course} ")

e1=student("Krishna",25,"arts")
print(e1)
