employee = {
    "id": 101,
    "name": "Anish",
    "salary": 900000.00,
    "department": "IT",
    "designation": "Project Manager",
    "projects": {"E-Commerce", "Hospital Management", "Vendor Application"}
}

print(employee)

# 1. by keys
print(employee.keys())

for key in employee.keys():
    print(f"{key}--{employee[key]}")

# 2. by values
print(employee.values())

for value in employee.values():
    print(value)

# 3. by items
print(employee.items())

for key, value in employee.items():
    print(f"{key}--{value}")