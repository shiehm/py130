"""
Write a function named later that takes two arguments: a function, func, and an 
argument for that function, argument. The return value should be a new function 
that calls func with argument as its argument. 
"""

def later(func, argument):
    def new_func():
        return func(argument)
    
    return new_func

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!


"""
Write a function named later2 that takes two arguments: a function, func, and an 
argument for that function, first_arg. The return value should be a new function 
that takes an argument, second_arg. The new function should call the func with 
the arguments provided by first_arg and second_arg. 
"""

def later2(func, first_arg):
    def inner(second_arg):
        return func(first_arg, second_arg)
    
    return inner

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!