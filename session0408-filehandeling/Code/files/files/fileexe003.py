#Reading writeing and updaing json file

# import json
# file=None
# try:
#     file = open("f:\Mithun-PythonCode\Python\Materials\session0408-filehandeling\Code\files\files\example.json", "r")
#     data = json.load(file)
#     print(data)
# except FileNotFoundError as e:
#     print(e)
# finally:
#     if file is not None:
#         file.close()

# import json

# file =None

# try:
#   file = open("f:\Mithun-PythonCode\Python\Materials\session0408-filehandeling\Code\files\files\example.json", "r")
#   data =json.load(file)
#   print(data)
# except FileExistsError as e:
#     print(e,"the file is not found,so please create file")    
# finally:

#     if file is not None:
#       file.close()

import json

file = None

try:
    file = open(
        r"F:\Mithun-PythonCode\Python\Materials\session0408-filehandeling\Code\files\files\example.json",
        "r"
    )

    data = json.load(file)
    print(data,["name"])
    print(data["age"])
    print(data["city"])
    print(data["isStudent"])

    print(data)

    

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Invalid JSON format.")

finally:
    if file is not None:
        file.close()