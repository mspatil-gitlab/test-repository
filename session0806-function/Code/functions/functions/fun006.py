# variable length parameters

def add(*numbers): # [20, 10] or [20, 10, 5] or [20, 10, 40, 50]
    total = 0
    for num in numbers:
        total = total + num
    
    return total

print(f"Sum: {add(20, 10)}")
print(f"Sum: {add(20, 10, 5)}")
print(f"Sum: {add(20, 10, 40, 50)}")