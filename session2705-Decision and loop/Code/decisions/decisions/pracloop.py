ch = input("Enter a character : ")
# print(f"You entered: {ch} and its type is {type(ch)} "
#       f"and its id is {id(ch)} and its memory size is {ch.__sizeof__()}")
# print(ch, ord(ch))
print("Enter a Character:", ord(ch))

if ord(ch) >= 97 and ord(ch) <= 122:   
    if ch in "aeiou":
        print("Vowel.")
    else:
        print("Consonant.")


# ch = ch.lower()
