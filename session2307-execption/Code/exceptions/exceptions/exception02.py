try:
    n1 = int(input("Enter number1: "))
    n2 = int(input("Enter number2: "))
    r = n1 / n2
    print(f"Result: {r}")
except ZeroDivisionError as ex:
    print(ex)
except ValueError as ex:
    print(ex)

print("End of the program.")