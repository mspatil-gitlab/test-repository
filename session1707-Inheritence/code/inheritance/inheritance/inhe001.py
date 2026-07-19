class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return(
            f"\nID: {self.id}"
            f"\nName: {self.name}"
        )

class Employee(Person):
    def __init__(self, id, name, salary, department):
        
        super().__init__(id, name)
        
        self.salary = salary
        self.department = department
    
    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nSalary: {self.salary}"
            f"\nDepartment: {self.department}"
        )

class Student(Person):
    def __init__(self, id, name, degree, grade):
        super().__init__(id, name)
        self.degree = degree
        self.grade = grade
    
    def __str__(self):
        return( 
            f"{super().__str__()}"
            f"\nDegree: {self.degree}"
            f"\nGrade: {self.grade}"
        )

class Customer(Person):
    def __init__(self, id, name, address, bill_amount):
       super().__init__(id, name)
       self.address = address
       self.bill_amount = bill_amount
    
    def __str__(self):
        return( 
            f"{super().__str__()}"
            f"\nAddress: {self.address}"
            f"\nBill Amount: {self.bill_amount}"
        )

e1 = Employee(101, "Mithun", 900000.00, "IT")
print(e1)

s1 = Student(1, "Anish", "B.Tech", "A+")
print(s1)

c1 = Customer("Cus001", "Rajesh","Bangalore-13", 2500)
print(c1)