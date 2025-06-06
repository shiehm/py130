"""
Problem: Create a Robot class that assigns a random name each time it is rebooted. 

Requirements:
- Names are generated randomly in a format: [A-Z][A-Z]\d\d\d
- Names are assigned the first time it is "booted up" and during "factory reset"
- We need a `name` property (str)
- We need a way to avoid name clashes for the randomly generated robot names 
- We need a random name generator

Data Structure: name will be a string

Algorithm:

`reset`:
1. run name_generator and set a variable to hold the return value
2. check if the name exists in the name universe, if not return it and add it 
3. if it is already existing, run the generator again

`name_generator`:
- This method should just return a string name 
1. set a `random_name` variable to ''
2. using string.ascii_uppercase as a selection set, add 2 random chars 
3. using string.digits as a set, add 3 random charts

"""

import re
import random
import string

class Robot:
    _existing_names = set()
    
    def __init__(self):
        self._name = None
    
    @property
    def name(self):
        if not self._name:
            self.reset()
        return self._name 
    
    def reset(self):
        if self._name:
            Robot._existing_names.remove(self._name)
            
        random_name = self.name_generator()
        while random_name in Robot._existing_names:
            random_name = self.name_generator()
        
        self._name = random_name
        Robot._existing_names.add(random_name)
        
        
    def name_generator(self):
        random_name = []
        random_name += random.choices(string.ascii_uppercase, k=2)
        random_name += random.choices(string.digits, k=3)
        return ''.join(random_name)