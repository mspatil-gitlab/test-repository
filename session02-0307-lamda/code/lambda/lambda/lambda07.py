

students = ["Divyaaa", "Anish", "Ramesh"]
sorted_students = sorted(students, key = lambda student: len(student))
print(sorted_students)


sorted_students = sorted(students, key = lambda student: len(student), reverse=True)
print(sorted_students)