"""
Use a generator expression to yield each character of a string in reverse order.
"""

lst = ['hi', 'my', 'name', 'is']
reverse = (word[::-1] for word in lst)
print(list(reverse))