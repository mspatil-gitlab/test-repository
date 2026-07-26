try:
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError as ex:
    print("Error (Division by Zero):", ex)
except ValueError as ex:
    print("Error (Invalid input format):", ex)
except Exception as ex:
    print("General Error:", ex)

print("End of the program")


