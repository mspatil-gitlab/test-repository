# user execption example 


class AgeExecption (Exception):
    pass


try:
    age = int(input("Enter age : "))
    if age < 18:
        raise AgeExecption

    print("You are eligible for voting")

except AgeExecption as ex:
    print("You are not eligible for voting")
except ValueError as ex:
    print("Error: Please enter a valid integer for age.")
finally:
    print("Thanks")

