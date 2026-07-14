class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y
    
    
c = Calculator()
print(f"Sum: {c.add(20, 10)}")
print(f"Subtraction: {c.sub(20, 10)}")