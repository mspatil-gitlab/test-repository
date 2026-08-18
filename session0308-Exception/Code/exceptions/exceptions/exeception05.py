
class AgeNotSufficientError(Exception):
    def __init__(self, age):
            self.age = age;
    def __str__(self):
        return f"Your age: {self.age}, so you are not eligible to vote."

try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        raise AgeNotSufficientError(age)
except AgeNotSufficientError as ex:
    print(ex)
