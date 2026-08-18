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

class truck(Vehicle):
    def __init__(self,make,model,colour,year):
        self.colour=colour
        self.year=year
        super().__init__(make,model)

    def __str__(self):
        return(f"{super().__str__()}\nColor: {self.colour}\nYear: {self.year}")      

t1 = truck("TATA","Safari","Yellow",2010)   
   
c1 =Car(f"Toyota","Corolla",4,2022)
print(c1)
print(t1)
        

        
