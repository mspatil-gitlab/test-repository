# keyword arguments

def display_employee(id, name, salary, designation):
    print("=================")
    print(f"ID: {id}, Name: {name}, Salary: {salary}, Designation: {designation}")

display_employee(101, "Anish", 900000.00, "Manager")

# display_employee("Rajesh", 102, "Accountant", 1000000.00)

display_employee(name="Rajesh", id=102, designation="Accountant", salary=1000000.00)
