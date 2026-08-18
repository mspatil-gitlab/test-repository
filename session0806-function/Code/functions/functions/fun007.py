# variable length parameters
# 2. variable length keyword arguments (**kwargs)

def display_details(**info):
    for k, v in info.items():
        print(f"{k}===>{v}")


display_details(name="Alice", age=30, city="New York")
