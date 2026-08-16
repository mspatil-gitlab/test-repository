file = open("f:\\Mithun-PythonCode\\Python\\Materials\\session0408-filehandeling\\Code\\files\\files\\example.txt","w")
file.write("hi this is new file created by python")
file.close()

file = open("f:\\Mithun-PythonCode\\Python\\Materials\\session0408-filehandeling\\Code\\files\\files\\example.txt","a")



file.write("\nthis is appended line")
file.close()

