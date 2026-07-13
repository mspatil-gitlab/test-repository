class Employee:
    def create_employee(self, id, name, salary, designation):
        self.id = id
        self.name = name
        self.salary = salary
        self.designation = designation
    
    def show_employee(self):
        print("==========================")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Designation: {self.designation}")

e1 = Employee()
e1.create_employee(101, "Mithun", 900000.00, "Manager");
e1.show_employee()

e2 = Employee()
e2.create_employee(102, "Divya", 800000.00, "Accountant");
e2.show_employee()

#empoyees = [Employee(), Employee(), Employee(), Employee(), Employee()]

