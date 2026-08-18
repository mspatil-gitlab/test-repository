# Tuple Packing and Unpacking

# packing
# person = ("John", 25, "Engineer")

person = "John", 25, "Engineer"
print(person)

'''name = person[0]
age = person[1]
designation = person[2]
'''
# un-packing
name, age, designation = person

print(f"{name}\n{age}\n{designation}")