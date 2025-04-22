"""
Write a function named combine that takes three positional arguments and returns 
a tuple containing all three. Call this function with three different values.
"""

# def combine(arg1, arg2, arg3):
#     return (arg1, arg2, arg3)

# print(combine(1, 2, 3))


"""
Define a function named multiply that accepts two positional-only arguments and 
returns their product. The function should not allow these parameters to be 
passed as keyword arguments.
"""

# def multiply(num1, num2, /):
#     return num1 * num2
    
# print(multiply(2, 4))


"""
Create a function named describe_pet that takes one positional argument 
animal_type and one keyword argument name with a default value of an empty 
string. The function should print a description of the pet. The function should 
not accept more than 1 positional argument.
"""

# def describe_pet(animal_type, *, name=''):
#     return f'You have an {animal_type} that is {name}'
    
# print(describe_pet("Hamster", name="Harry"))


"""
Write a function named calculate_average that any number of numeric arguments 
and returns their average. Make sure it returns None if no arguments are provided.
"""

# def calculate_average(*args):
#     return sum(args) / len(args) if args else None

# print(calculate_average(1, 2, 3, 4, 5, 6, 7, 8))
# print(calculate_average())


"""
Create a function named find_person that accepts any number of keyword arguments
in which each key is someone's name and the value is their associated profession. 
The function should check whether any of the key/value pairs has a key of 
"Antonina" and then, if the key is found, print a message that shows Antonina's 
profession. Otherwise, it should say "Antonina not found". The function should 
not accept any positional arguments.
"""

# def find_person(**kwargs):
#     if 'Antonina' in kwargs:
#         print(kwargs['Antonina'])
#     else:
#         print('Antonina not found')

# find_person(John="Engineer", Antonina="Software Engineer")
# # Antonina's profession is Software Engineer

# find_person(John="Engineer", Ginni="Software Engineer")
# # Antonina not found


"""
Define a function named concat_strings that takes any number of strings and 
returns the concatenation of all the strings. Add a keyword-only argument sep 
with a default value of ' ' that specifies the separator to use between the strings.
"""

# def concat_strings(*args, sep=' '):
#     return sep.join(args)

# print(concat_strings('hi', 'my', 'name', 'is', sep='--'))


"""
Create a function named register that takes exactly three arguments: username 
as positional-only, password as keyword-only, and age as either a positional 
or keyword argument.
"""

# def register(username, /, age, *, password):
#     print(f'{username} is {age} years old, here is the password: {password}.')
    
# register('Melvin', 22, password='SamIYam')
# register('Melvin', age=22, password='SamIYam')
# # register('Melvin', 22, 'SamIYam')


"""
Create a function named print_message that requires a keyword-only argument
(message) and an optional keyword-only argument (level) with a default value of 
"INFO". The function should print out the message prefixed with the level. The 
function shouldn't accept any positional arguments.
"""

# def print_message(*, message, level='INFO'):
#     print(f'{level}: {message}')

# print_message(message="This is a test message.", level="WARNING")
# # [WARNING] This is a test message.

# print_message(message="This is an informational message.")
# # [INFO] This is an informational message.

# print_message()