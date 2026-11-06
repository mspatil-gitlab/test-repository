file = None
try:
    file = open("example.txt","w")
    #file.write("Hello dear friends.")
    #file.write("\nWhere are you people?")

    lst = ["Hi Mithun.\n", "How is rain today?\n", "I hope you are good now.\n"]
    file.writelines(lst)
except FileNotFoundError as e:
    print(e)
finally:
    if file != None:
        file.close()
