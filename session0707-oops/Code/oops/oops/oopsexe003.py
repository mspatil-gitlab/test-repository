class employee_address:
    def __init__(self,id,city,state,country):
        self.id=id
        self.city=city
        self.state=state
        self.country=country
    
    def __str__(self):
        # return f"{self.id}, {self.city}, {self.state}, {self.country}"

        return f"\n==========================\nID: {self.id}\nCity: {self.city}\nState: {self.state}\nCountry: {self.country}"
    

e1=employee_address(101,"Mysore","Karnataka","India")
print("\n=================",e1)
