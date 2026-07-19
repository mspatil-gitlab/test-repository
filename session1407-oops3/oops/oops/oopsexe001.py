#Create a class Car with attributes
#make, model, and year.
#Define a method car_info() that prints out the details of the car. Then, create an instance of the class and print the car information.

class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def car_info(self):
        return f"{self.make} {self.model} {self.year}"

c1=car("TOYOTA","COROLLA",2024)
print(c1.car_info())

    