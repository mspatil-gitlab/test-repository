'''def add(n1, n2):
    return n1 + n2

print(add(20, 10))
'''

add = lambda n1, n2: n1 + n2
sub = lambda k1,k2 :k1 - k2
div = lambda d1,d2 :d1 / d2


print("Addition:", add(20, 10))

print("Subtraction:", sub(35, 10))
print("Division:", div(35, 10)) 

print("Multiplication:", (lambda m1,m2 : m1 * m2)(5, 10))