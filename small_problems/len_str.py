"""
Use map to create a list of lengths of each string in the original list.
"""
lst = ['hi', 'my', 'name', 'is']
lengths = map(len, lst)
print(list(lengths))