# recursion
# a function calls itself

'''def fun():
    print("Hi Dear")
    fun()

fun()
'''

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(f"Factorial: {factorial(5)}")