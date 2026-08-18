'''def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]
square_numbers = []

for num in numbers:
    square_numbers.append(square(num))

print(square_numbers)
'''

'''def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]

squares = list(map(square, numbers))
print(squares)
'''

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x : x ** 2, numbers))
print(squares)

