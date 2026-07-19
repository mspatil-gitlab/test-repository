#Exercise 5: Method Overloading (Simulating)
#Problem:
#Create a class Rectangle with a method area(). 
# If one argument is passed, it calculates the area of a square (side^2), and if two arguments are passed, it calculates the area of a rectangle (length * width).
# (Python does not support traditional method overloading, but we can simulate it by checking the number of arguments passed.)

# Creating an object of Rectangle class

# Calculating area of square

# Calculating area of rectangle


class Rectangle():
    def area(self,length=0,width=0):
        if length==0 and width==0:
            return "No arguments passed"
        elif length!=0 and width==0:
            return length*length
        else:
            return length*width

#Creating an object of Rectangle class
r1=Rectangle()
#Calculating area of square
print(f"Area of square: {r1.area(5)}")
#Calculating area of rectangle
print(f"Area of rectangle: {r1.area(5,10)}")    

