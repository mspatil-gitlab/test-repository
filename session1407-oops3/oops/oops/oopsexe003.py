#Create a Book class with the attributes title, author, and price. Implement a method apply_discount() that applies a 10% discount to the price.
# Then, create an instance of Book, apply the discount, and print the updated price.


class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def apply_discount(self):
        self.price=self.price-(self.price*0.1)

    def __str__(self):
        return f"{self.title} {self.author} {self.price}"
    
b1=book("Python","Mithun",1000)
print(b1.price)
b1.apply_discount()
print(b1.price)
