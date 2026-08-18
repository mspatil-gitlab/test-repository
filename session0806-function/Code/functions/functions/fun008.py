
count = 0

def increment():
    global count
    count = count + 1


increment()
increment()
increment()
for i in range(5,1,-1):
    increment()

print(f"Final value: {count}")
