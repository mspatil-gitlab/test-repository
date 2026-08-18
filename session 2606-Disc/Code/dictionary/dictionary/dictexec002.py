person = {"name": "John", "age": 30, "city": "New York"}
""
Bank ={"name":"Bank of India","city":"Bangalore","maxloan":10000}

# Iterate through keys
for key in person:
    print(key, "->", person[key])

    for key2 in Bank:
        print(key,"->", Bank[key2])
