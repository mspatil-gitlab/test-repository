# program to find an element is there in a list (searching)

numbers = []

size = int(input("Enter the size: "))
for i in range(0, size):
    num = int(input("Enter a number: "))
    numbers.append(num)


f = int(input("Enter a number to find: "))

is_found = False

for num in numbers:
    if num == f:
        print("Found.")
        is_found = True
        break

if is_found == False:
    print("Not found.")