class employee:
    def __init__(self,id,name,city,salary,grade,designation):
        self.id = id
        self.name = name
        self.city = city
        self.salary = salary
        self.grade = grade
        self.designation = designation

    def __str__(self):
        return (
            "\n=========================="
            f"\nID: {self.id}"
            f"\nName: {self.name}"
            f"\nCity: {self.city}"
            f"\nSalary: {self.salary}"
            f"\nGrade: {self.grade}"
            f"\nDesignation:{self.designation}"
        )

e1 = employee(101, "Harish", "Mysore", 25000, "A", "Manager")
print(e1)
