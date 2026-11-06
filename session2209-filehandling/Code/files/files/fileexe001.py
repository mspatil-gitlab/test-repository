import pickle
import os

class Product:
    def __init__(self,id,name,price,category):
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

p1 = Product(1,"Mobile",25000.00,"Electronics")
p2 = Product(2,"Laptop",55000.00,"Electronics")
p3 = Product(3,"Mobile",65000.00,"Electronics")

# with open("products.dat","wb") as file:
#     pickle.dump(p1,file)
#     pickle.dump(p2,file)
#     pickle.dump(p3,file)

#     print("Products saved to products.dat")

with open("products.dat","rb") as file:
    while True:
        try:
            p = pickle.load(file)
            print(p)
        except EOFError:
            break

if os.path.exists("products.dat"):
    os.remove("products.dat")

            
