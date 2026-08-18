# reverse of a number
# ip: 1234, op:4321

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    rem = num % 10
    reverse = reverse * 10 + rem
    num = num // 10

print("Reverse: ", reverse)

'''
reverse = 0
num = 1234

1. rem = 1234 % 10 = 4

reverse = reverse * 10 + rem
        = 0 * 10 + 4 = 0 + 4 =  4

    1234 // 10 = 123

2. rem = 123 % 10 = 3

reverse = reverse * 10 + rem
        = 4 * 10 + 3 = 40 + 3 = 43 
123 // 10 = 12


3. rem = 12 % 10 = 2
reverse = reverse * 10 + rem
        = 43 * 10 + 2 = 430 + 2 = 432

12 // 10 = 1

4.rem = 1 % 10 = 1
reverse = reverse * 10 + rem
        = 432 * 10 + 1 = 4320 + 1 = 4321
1 // 10 = 0

'''
