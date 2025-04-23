"""
Create a list where each number from the original list 
is squared using the map method.
"""

lst = list(range(1,11))
squares = map(lambda x: x**2, lst)
print(list(squares))