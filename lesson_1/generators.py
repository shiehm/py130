"""
Create a generator expression that generates the reciprocals of the numbers 
from 1 to 10. A reciprocal of a number n is 1 / n. 
Use a for loop to print each value.
"""

# reciprocals = (1 / num for num in range(1, 11))
# for num in reciprocals:
#     print(num)

"""
Create a generator function that generates the reciprocals of the numbers from 
1 to n, where n is an argument to the function. 
Use a for loop to print each value.
"""

# def reciprocals(n):
#     for num in range(1, n + 1):
#         yield 1 / num
        
# for num in reciprocals(10):
#     print(num)

"""
Use a generator expression to capitalize every string in a list of strings. 
Use a single print invocation to print all the capitalized strings as a tuple.
"""

# list_of_strings = ['hi', 'my', 'name', 'is']
# generator = (string.capitalize() for string in list_of_strings)
# print(tuple(generator))

"""
Create a generator function that generates the capitalized version of every 
string in a list of strings. Use a single print invocation to print all the 
capitalized strings as a tuple.

"""

list_of_strings = ['hi', 'my', 'name', 'is']
def capitalize(list_of_strings):
    for string in list_of_strings:
        yield string.capitalize()

print(tuple(capitalize(list_of_strings)))

"""
Use a generator expression to capitalize the strings in a list of strings whose 
length is at least 5. Use a single print invocation to print all the capitalized 
strings as a set.
"""

# list_of_strings = ['hi', 'my', 'name', 'is', 'melvin']
# capitalize = (string.capitalize() for string in list_of_strings if len(string) >= 5)
# print(set(capitalize))

"""
Create a generator function that generates the capitalized version of every 
string in a list of strings whose length is less than 5. Use a single print 
invocation to print all the capitalized strings as a set.
"""

# list_of_strings = ['hi', 'my', 'name', 'is', 'melvin']
# def capitalize_lt_5(list_of_strings):
#     for string in list_of_strings:
#         if len(string) < 5:
#             yield string.capitalize()

# print(set(capitalize_lt_5(list_of_strings)))