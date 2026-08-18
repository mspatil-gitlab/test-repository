from functools import reduce


number =[20,60,20,90,10]

sqr_number= list(map(lambda x:x **2,number))
print(f"Square number",sqr_number)

product_number = reduce(lambda x, y: x * y, number)


print(f"Product number",product_number)
