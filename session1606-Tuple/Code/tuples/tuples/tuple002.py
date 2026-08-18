# accessing tuple elements
'''colors = ("red", "green", "blue", "yellow")

print(colors[0])   # Output: red
print(colors[-1])  # Output: yellow (last element)
'''

# tuple slicing

'''numbers = (10, 20, 30, 40, 50, 60)
print(numbers)
print(numbers[0:6])
print(numbers[:])
print(numbers[1:4])

print(numbers[:3])   # Output: (10, 20, 30)
print(numbers[-3:])  # Output: (40, 50, 60)
'''

'''animals = ("cat", "dog", "elephant")

for animal in animals:
    print(animal)

for i in range(0, len(animals)):
    print(animals[i])

for i in range(len(animals)-1, -1, -1):
    print(animals[i])
'''

# Tuple Methods
numbers = (1, 2, 3, 4, 2, 5, 2)

# count
print(numbers.count(2))
print(numbers.count(9))

# index
print(numbers.index(2))
print(numbers.index(9))
