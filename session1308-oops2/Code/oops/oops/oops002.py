class Employee:
    def __init__(self, id, name, salary, designation):
        self.id = id
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def __str__(self):
        return (
            "\n=========================="
            f"\nID: {self.id}"
            f"\nName: {self.name}"
            f"\nSalary: {self.salary}"
            f"\nDesignation: {self.designation}"
        )
        

e1 = Employee(101, "Mithun", 900000.00, "Manager")
print(e1)

e2 = Employee(102, "Divya", 800000.00, "Accountant")
print(e2)