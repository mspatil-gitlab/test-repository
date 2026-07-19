class Employee:
    concern_name = "TCS" # class variable
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        #self.concern_name = "TCS"
    
    @classmethod
    def get_concern_name(cls): # class method
        return cls.concern_name
    
    def __str__(self):
        return(
            f"\nID: {self.id}"
            f"\nName: {self.name}"
            f"\nSalary: {self.salary}"    
        )

employees = [
    Employee(1, "Anish", 900000.00),
    Employee(2, "Divya", 1000000.00),
    Employee(3, "Rajesh", 400000.00),
    ]

print(f"The following employees are of {Employee.get_concern_name()}.")

for employee in employees:
    print(employee)