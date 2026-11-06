import pickle

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return(
            f"\nID: {self.id}"
            f"\nName: {self.name}"
            f"\nPrice: {self.price}"
            f"\nCategory: {self.category}"
        )


'''p1 = Product(1, "Mobile", 25000.00, "Electronics")

with open("products.ser", "wb") as file:
    pickle.dump(p1, file)
'''

with open("products.ser", "rb") as file:
    p1 = pickle.load(file)

print(p1)
