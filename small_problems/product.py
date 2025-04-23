"""
Calculate the product of all numbers in a list using the reduce function.
"""

from functools import reduce

lst = list(range(1,6))
def product(a, b):
    return a * b
    
print(reduce(product, lst))

print(reduce(lambda x, y: x * y, lst))