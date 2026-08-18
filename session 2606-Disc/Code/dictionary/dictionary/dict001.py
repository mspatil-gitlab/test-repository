# key and value
employee = {
    "id": 101,
    "name": "Anish",
    "salary": 900000.00,
    "department": "IT",
    "designation": "Project Manager",
    "projects": {"E-Commerce", "Hospital Management", "Vendor Application"}
}

employee["department"] = "Information Technology"

print(employee)
print(f"Name: {employee["name"]}")
print(f"The employee '{employee["name"]}' is working in '{employee["department"]}'.")