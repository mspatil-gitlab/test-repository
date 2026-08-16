try:
    with open("example.txt", "r") as file:
        # content = file.read()
        # content = file.readline()
        content = file.readlines()

        for line in content:
            print(line.replace("\n", ""))
except FileNotFoundError as e:
    print(e)
