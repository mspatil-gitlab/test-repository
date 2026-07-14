# class Employee:
#     concern_name = "TCS" # class variable
#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         #self.concern_name = "TCS"
    
#     @classmethod
#     def get_concern_name(cls): # class method
#         return cls.concern_name
    
#     def __str__(self):
#         return(
#             f"\nID: {self.id}"
#             f"\nName: {self.name}"
#             f"\nSalary: {self.salary}"    
#         )

# employees = [
#     Employee(1, "Anish", 900000.00),
#     Employee(2, "Divya", 1000000.00),
#     Employee(3, "Rajesh", 400000.00),
#     ]

# print(f"The following employees are of {Employee.get_concern_name()}.")

# for employee in employees:
#     print(employee)

class Student :
    school_name="National school"
    school_area ="MUMBAI"


    def __init__(self,id,name,age,courses):
        self.id = id
        self.name=name
        self.age=age
        self.courses = courses

    @classmethod
    def get_schoolname(cls): # class method
        return cls.school_name
    def __str__(self):
        return(
            f"\nID: {self.id}"
            f"\nName: {self.name}"
            f"\nAge: {self.age}"
            f"\nCourses: {self.courses}"  
        )
    
studentsinformatio = [
        Student(1, "Anish", 20, ["Math", "Physics"]),
        Student(2, "Divya", 21, ["Chemistry", "Biology"]),
        Student(3, "Rajesh", 22, ["Computer Science", "IT"]),
        ]

print("==================================================")
print(f"The following students are of {Student.get_schoolname()}")

print("==================================================")

print(f"Area of the school: {Student.school_area}")

for student in studentsinformatio:
        print(student)

    
    





