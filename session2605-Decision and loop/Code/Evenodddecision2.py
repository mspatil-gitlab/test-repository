number = int(input("Enter a number: "))
if number < 0:
    print("Negative number.")
if number !=0:
    if number % 2 == 0:
        print("Even.")
    else:
        print("Odd.")
else:
    print("Wrong input.")