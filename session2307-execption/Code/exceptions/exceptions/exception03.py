'''n=None
print(n**2)
'''

'''n1 = "100"
n2 = "200"
try:
    r = n1 - n2
    print(r)
except TypeError as ex:
    print(ex)
'''


try:
    nums = [1, 2, 3, 4, 5]
    print(nums[5])
except IndexError as ex:
    print(ex)