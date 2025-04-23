"""
Remove all None values from a list using the filter method.
"""
lst = [None, 'hi', 1, 2, 3, None, 'bye']
new_lst = list(filter(lambda x: x != None, lst))
print(new_lst)
