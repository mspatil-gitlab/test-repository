
# Creation of a dictionary with key and value pairs , nameofemlployee ,id, salary, department, designation and projects,city

employee = {
    "id": 101,
    "name": "John Doe",
    "salary": 50000,
    "department": "Engineering",
    "designation": "Software Engineer",
    "projects": ["Project A", "Project B"],
    "city": "New York",
    "Team":"testing"

}
# print(employee)
# #need to slice the dictionary with only projectA

# projectA = employee["projects"][0]
# print(f"Project A of the employee is: {projectA}")

# print(f"Nam of the employee with project A is",employee["projects"][0])

print(f"These are key :{employee.keys()}", sep="\n")


print(*employee.keys() , sep="\n")

print(f"These are values :{employee.values()}", sep="\n")

print(*employee.values(), sep="\n")

for key, value in employee.items():
    print(f"{key}-->{value}")    

student ={"name":"mithun","rollno":104,"age":20,"subject":"Commerce"}

print(f"Below mentioned student details are:\n{student}")




  

