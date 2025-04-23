"""
Obtain only the even numbers from a list using the filter function.
"""

lst = list(range(1,11))
def is_even(num):
    return num % 2 == 0

evens = filter(is_even, lst)
print(list(evens))

even = filter(lambda x: x % 2 == 0, lst)
print(list(even))