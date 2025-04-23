"""
Use reduce to concatenate a list of strings into a single string.
"""

from functools import reduce

lst = ['hi', 'my', 'name', 'is']
def concat(a, b):
    return a + b
string = reduce(concat, lst)
print(string)