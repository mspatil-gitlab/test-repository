customer = {
    "id": 101,
    "name": "Ravi Kumar",
    "address": "Hyderabad, Telangana",
    "products": ["Laptop", "Mouse", "Keyboard"],
    "order_amount": 68500
}

print(customer.get("products"))
print(customer.get("products")[1])

print(customer.get("discount", 0))

print(customer.get("order_amount", 58500))
print(customer)

customer.update({"country": "India"})
print(customer)

print("==============\n")
print(customer.pop("address"))
print(customer)

print(customer.popitem())

customer.clear()
print(customer)

