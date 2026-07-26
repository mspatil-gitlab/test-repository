try:
    n1 = int(input("Enter number1: "))
    n2 = int(input("Enter number2: "))
    r = n1 / n2 
except ZeroDivisionError as ex:
    print(ex)
except ValueError as ex:
    print(ex)
else:
    print(f"Result: {r}")
finally:
    print("This executes when exception is there or not there.")

print("End of the program.")