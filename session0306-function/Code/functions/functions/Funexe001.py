# def Daydisplayshow(day):
#     print(f"Day to display is:{day}")

# Daydisplayshow("Monday")
# Daydisplayshow("Tuesday")
# Daydisplayshow("Wednesday")
# Daydisplayshow("Thursday")
# Daydisplayshow("Friday")

# Function with return value
# def greet(name):

#     # print(f"Hello How are you{name}?")
#     return f"Hello How are you {name}?"
# # There are two ways to call a function with return value
# # 1. Store the return value in a variable and then print it
# message = greet("Mithun")
# print(message)
# # 2. Directly print the return value of the function

# print(greet("Mithun"))

# Def sum(num1,numb2):
# return num1 + num2
# def sum(num1, num2):
#     return num1 + num2

# # Returning multiple values from a function
# result = sum(5, 10)
# print(result)

# def display_message():
#     print("Welcome to Python")

# display_message()

# def introduceshow(name,age):

#     print(f"myname is {name} and my age is {age}")
# introduceshow("Mithun", 25)


# args concept

def add(*number):
     return sum(number)

print(add(1, 2, 3, 4, 5))



# def sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# result = sum(1, 2, 3, 4, 5)
# print(result)

# # When not sure with number of aurguments * args
# def display_names(*names):
#     for name in names:
#         print(name)

# display_names("X1", "X2", "X3")

#What is a Closure Function

# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function

# closure = outer_function(10)
# print(closure(5))

def bonus_calculator(rate):
    def calculate(salary):
        return salary * rate
    return calculate
bonus_10_percent = bonus_calculator(0.1)
print(bonus_10_percent(50000))  
