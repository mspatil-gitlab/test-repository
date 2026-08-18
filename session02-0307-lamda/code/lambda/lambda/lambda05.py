

'''numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total = total + num

print(total)
'''

from functools import reduce

'''def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]

total = reduce(add, numbers)
print(total)
'''

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)

print(total)