class Vehicle():
    def __init__(self,make,model):
        self.make =make
        self.model =model

    def __str__(self):
        return(f"Make: {self.make}\nModel: {self.model}")

class Car(Vehicle):
    def __init__(self,make,model,num_doors,year):
        super().__init__(make,model)
        self.num_doors = num_doors
        self.year = year

    def __str__(self):
        return(f"{super().__str__()}\nNumber of doors: {self.num_doors}\nYear: {self.year}")    
        

make = input("Enter Make: ")
model = input("Enter Model: ")
num_doors = int(input("Enter Number of Doors: "))
year = int(input("Enter Year: "))

c1 = Car(make, model, num_doors, year)
print("\n--- Car Details ---")
print(c1)