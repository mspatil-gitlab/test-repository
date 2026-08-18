
count = 0

def increment():
    global count
    count = count + 1


increment()
increment()
increment()


print(f"Final value: {count}")
