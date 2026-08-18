'''def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)
'''

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

