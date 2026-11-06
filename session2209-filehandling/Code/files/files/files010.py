import pickle
import os


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.product_id:<10} {self.name:<20} {self.price}"


FILE_NAME = "products.dat"


# -------------------------------------------------
# CREATE
# -------------------------------------------------

def create_product():

    product_id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))

    products = read_all_products()

    # Check duplicate ID
    for product in products:
        if product.product_id == product_id:
            print("Product ID already exists.")
            return

    product = Product(product_id, name, price)

    products.append(product)

    save_all_products(products)

    print("Product created successfully.")


# -------------------------------------------------
# READ
# -------------------------------------------------

def read_all_products():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "rb") as file:

        try:
            products = pickle.load(file)
            return products

        except EOFError:
            return []


def display_products():

    products = read_all_products()

    if len(products) == 0:
        print("No products found.")
        return

    print("\nID         Name                 Price")
    print("------------------------------------------")

    for product in products:
        print(product)


# -------------------------------------------------
# UPDATE
# -------------------------------------------------

def update_product():

    product_id = int(input("Enter product ID to update: "))

    products = read_all_products()

    for product in products:

        if product.product_id == product_id:

            print("Current details:")
            print(product)

            product.name = input("Enter new product name: ")
            product.price = float(input("Enter new product price: "))

            save_all_products(products)

            print("Product updated successfully.")
            return

    print("Product not found.")


# -------------------------------------------------
# DELETE
# -------------------------------------------------

def delete_product():

    product_id = int(input("Enter product ID to delete: "))

    products = read_all_products()

    for product in products:

        if product.product_id == product_id:

            products.remove(product)

            save_all_products(products)

            print("Product deleted successfully.")
            return

    print("Product not found.")


# -------------------------------------------------
# SAVE OBJECTS TO FILE
# -------------------------------------------------

def save_all_products(products):

    with open(FILE_NAME, "wb") as file:
        pickle.dump(products, file)


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

while True:

    print("\n===== PRODUCT MANAGEMENT SYSTEM =====")

    print("1. Create Product")
    print("2. Read Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_product()

    elif choice == 2:
        display_products()

    elif choice == 3:
        update_product()

    elif choice == 4:
        delete_product()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
