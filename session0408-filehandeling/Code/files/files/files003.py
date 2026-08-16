file = None
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print(e)
finally:
    if file != None:
        file.close()
    