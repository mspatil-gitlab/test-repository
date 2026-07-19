class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return (
            f"\nID: {self.id}"
            f"\nName: {self.name}"
            f"\nSalary: {self.salary}"
        )

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def __str__(self):
        emps = ""
        for employee in self.employees:
            emps = str(employee) + ", " + emps

        return(
            f"\nDepartment: {self.name}"
            f"\nEmployees: {emps}"

        )
    


e1 = Employee(1, "Anish", 900000.00)
e2 = Employee(2, "Divya", 800000.00)
e3 = Employee(3, "Rajesh", 700000.00)
e4 = Employee(4, "Mahesh", 1000000.00)
e5 = Employee(5, "Raghav", 300000.00)

employees = [e1, e2, e3, e4]

d1 = Department("IT", employees)
d1.add_employee(e5)
print(d1)