ch = input("Enter a character: ")
# print(ch, ord(ch))
ch = ch.lower()

# if ch in  'abacdefghijklmnopqrstuvwxyz':
if ord(ch) >= 97 and ord(ch) <= 122:
    if ch in "aeiou":
        print("Vowel.")
    else:
        print("Consonant.")
else:
    print("Invalid input.")
