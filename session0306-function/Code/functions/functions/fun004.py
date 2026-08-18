def greet(name="Chandru"):
    print(f"Hello {name}.")

greet("Mithun")
greet()

def greet_message(name, message="When are you coming?", address="BTM Layout"):
    print(f"Hello {name}. {message}. Address: {address}")

greet_message("Mithun", "How are you?")
greet_message("Chandru")
greet_message("Divya", "Malleswaram")

def add(n1, n2=20):
    return n1 + n2

print(add(100, 200))
print(add(1000))

