"""
Use nested generator expressions to create a flat list of numbers from a list of lists.
"""

lst_lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    
flat = (num for lst in lst_lst for num in lst)
print(list(flat))