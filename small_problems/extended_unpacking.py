"""
Unpack values from a tuple of four elements, but only keep the first and last values.
"""

data = (100, 200, 300, 400)
first, *_, last = data
print(first, last)
print(*_)
print(_)


"""
Unpack the first two elements from a list and store the remaining elements in another list.
"""
numbers = [1, 2, 3, 4, 5, 6]
first, *mid, last = numbers
lst = list(mid)
print(*mid)
print(first, lst, last)


"""
Given a nested tuple data = ((1, 2), (3, 4), (5, 6)), write a code to unpack 
this tuple into individual variables a, b, c, d, e, f.
"""
data = ((1, 2), (3, 4), (5, 6))
(a, b), (c, d), (e, f) = data
print(a, b, c, d, e, f)