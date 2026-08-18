# program to find sum and average

numbers = []

size = int(input("Enter the size: "))
for i in range(0, size):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0
for number in numbers:
    total = total + number

print(f"Sum: {total}")