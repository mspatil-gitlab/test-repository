# file = None
# try:
#     file = open("f:\\Mithun-PythonCode\\Python\\Materials\\session0408-filehandeling\\Code\\files\\files\\example.txt","r" )
#     print(file.read())
#     lst =("This is new edited line")  
#     print(file.read())
#     # i would now like to write to this file with lst content
#     print(file.writelines(lst))
#     print(file.read())
      

# except FileExistsError as e:
#     print(e)    

# if file is not None:
#     file.close()
   
file = None
try:
    # 1. Open the file in "r+" mode to allow both reading and writing
    file = open("f:\\Mithun-PythonCode\\Python\\Materials\\session0408-filehandeling\\Code\\files\\files\\example.txt", "r+")
    
    print("--- File Content Before Writing ---")
    print(file.read())
    
    # 2. To append to the end of the file, we write. Since we read to the end,
    # the cursor is already at the end of the file.
    lst = "\nThis is new edited line"  
    file.write(lst)  # Use write() instead of writelines() for a single string
    
    # 3. To read the file again from the beginning, we must seek back to 0
    file.seek(0)
    print("--- File Content After Writing ---")
    print(file.read())

except FileNotFoundError as e:  # FileNotFoundError is raised if the file doesn't exist
    print(e)    
finally:
    if file is not None:
        file.close()
