"""
Create a generator function that yields numbers from 1 to 5.
"""

def basic_gen():
    for num in range(1, 6):
        yield num
        
print([num for num in basic_gen()])