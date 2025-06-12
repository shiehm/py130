"""
Problem: Create your own todolist application. 

Requirements:
- We need an object class for Todo objects
- And a class for Todo List objects
- The Todo objects need to have a 
    - name
    - checkbox [ ] [x]
    - method to check or uncheck the boxes
- The Todolist object needs
    - name
    - str method that prints with a header, and prints the Todos
    - methods to add and remove todos 
    - methods to check all, uncheck all 
"""


class Todo:
    DONE = '[X]'
    NOT_DONE = '[ ]'
    
    def __init__(self, name):
        self.name = name
        self.check = Todo.NOT_DONE
    
    def __str__(self):
        return f'{self.check} {self.name}'
    
    def check(self):
        self.check = Todo.DONE
        
    def uncheck(self):
        self.check = Todo.NOT_DONE

class Todolist:
    pass