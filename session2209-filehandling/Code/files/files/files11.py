import pickle
class student:
    def __init__(self,name,marks,city):
        self.name = name
        self.marks = marks
        self.city = city
        
    
    def __str__(self):
        return (
            f"{self.name} ({self.marks} ({self.city}))"
        )

s1 = student("Raj", 85,"Hyd")
s2 = student("Mithun", 95,"vik")
s3 = student("Sunil",80,"CHe")

# save data in file

with open("student.txt","wb") as file:
    # pickle.dump(s1,file)
    # pickle.dump(s2,file)
    pickle.dump(s3,file)
    print("Students Saved.")
    print(f"First student data in file is {s1.name} {s1.marks} {s1.city}")
print(s1)
print(s2)
print(s3)

# read data from file
# with open("student.txt","rb") as file:
    
#     # p = pickle.load(file)
#     # print(p)

#     while True:
#         try:
#             p = pickle.load(file)
#             print(p)
#         except EOFError:
#             break
