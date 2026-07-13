class employee :
    def create_employee(self,id,name,city,salary,grade,designation):
        self.id = id
        self.name = name
        self.city = city
        self.salary = salary
        self.grade = grade
        self.designation = designation

    def display_employee(self):
        print("==========================")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Salary: {self.salary}")
        print(f"Grade: {self.grade}")
        print(f"Designation:{self.designation}")

        
l1 = employee()
l2 = employee()


l1.create_employee(101, "Harish", "Mysore", 25000,"A", "Manager")
l2.create_employee(102,"suresh", "banglore", 30000,"B", "Developer")

l1.display_employee()
l2.display_employee()





