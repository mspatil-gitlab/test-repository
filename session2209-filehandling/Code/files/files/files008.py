with open("example.txt", "r") as file:
    print("Initial Position: ", file.tell())
    print("First 5 characters: ", file.read(5))
    print("Now Position: ", file.tell())
    file.seek(0)
    print("First 5 characters: ", file.read(5))