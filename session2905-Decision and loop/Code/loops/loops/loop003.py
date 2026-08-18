# factorial of a number
n = int(input("Enter a number to find factorial: "))

fact = 1
for i in range(2, n+1):
    fact = fact * i

print(fact)




'''
5
!5 = 5 * 4 * 3 * 2 * 1
   = 1 * 2 * 3 * 4 * 5
   = 2 * 3 * 4 * 5
   = 120
'''