'''n1 = 10
n2 = 20
print("Before swap: ", n1, n2)

t = n1
n1 = n2
n2 = t
print("After swap: ", n1, n2)
'''

n1 = 10
n2 = 20
print(f"Before swap: {n1}, {n2}")

n1, n2 = n2, n1
print(f"After swap: {n1}, {n2}")