'''def get_marks(student):
    return student[1]

students = [('John', 85, "Bangalore"), ('Alice', 92, "Tirupati"), ('Bob', 78, "Mumbai")]
students.sort(key=get_marks)
print(students)
'''

students = [('John', 85, "Bangalore"), ('Alice', 92, "Tirupati"), ('Bob', 78, "Mumbai")]
students.sort(key=lambda s: s[1])
print(students)

students.sort(key=lambda s: s[1], reverse=True)
print(students)