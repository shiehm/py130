"""
Problem: Make your own map function that takes a callback function and applies
it to each element in an iterable and returns it in the same format 

Data Structure: List, other iterables 

Pseudo-code:
1. Create an empty results list
2. For every element in an iterable:
3. Invoke the callback with the current element as the argument.
4. Append the return value of the callback to the results list.
5. Return the results list.
"""

def custom_map(callback, iterable):
    results = []
    for element in iterable: 
        results.append(callback(element))
    return results
    
def custom_square(num):
    return num**2

print(custom_map(custom_square, range(1,10)))
print(custom_map(lambda number: number + 2, range(1,10)))