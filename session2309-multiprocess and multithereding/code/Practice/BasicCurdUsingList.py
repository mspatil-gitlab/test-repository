# Basic CRUD using List
# Student is just a List
students = [
    # {"id": 1, "name": "Ravi", "marks": 85},
    # {"id": 2, "name": "Priya", "marks": 90}
]

# Create Student Data using Dictionary

def create_student():
    student_id = int(input("Enter Student id: "))
    student_name = input("Enter Name: ")
    student_marks = int(input("Enter marks: "))

    list_db = {
        "id": student_id,
        "name": student_name,
        "marks": student_marks
    }

    students.append(list_db)  # append to 'students' list, NOT 'create_student'

    print("Student data Added Successfully!")
    print("All Students:", students)


create_student()

# Read Student Data
def read_student():
    print("Student Data:", students)
    if not students:
        print("No student data available.")
        return

    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")


read_student()