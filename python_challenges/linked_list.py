"""
Problem: Write a simple linked list implementation. 
- Each element in the list contains data and a "next" field pointing to the 
next element in the list of elements. This variant of linked lists is often 
used to represent sequences or push-down stacks (also called a LIFO stack).
- Provide methods to reverse and convert a linked list to/from a list.

Requirements (Element):
- needs a is_tail() method, testing whether it is the last element?
- datum property that gives value stored?
- next property to give the linked element that is next

Requirements (SimpleLinkedList):
- size property that gives length of the list as int
- is_empty() method
- push() method that appends an element to the list
- peek() method that... gives preview of last element pushed / the head of LIFO
- head property that gives the top of the LIFO stack
- pop() should work exactly the same way as a list
- from_list() method that returns a linked list w/ inx 0 as head (also convert None)
- to_list() method that converts linked list to regular list (return new list)
- elements are Element objects
- reverse() method returns the linked list in reverse

Data Structures:
- SimpleLinkedList should take in a list and convert its elements to Elements

Element class:
- This is just a node class, so it only needs 2 attributes: datum and next 
- datum is the actual value to be stored
- next is initialized as None and will be overwritten in the SimpleLinkedList 
if there are new items added

Algorithm for SimpleLinkedList initialization:
Based on test cases it seems like this is initialized with no arguments 
1. Set size attribute to 0 and head attribute to None

Algorithm for push:
1. initialize new_element and set it equal to Element(item) to be pushed
2. set the next attribute of new_element to the last element (head) 
3. set self.head = this element

Note: Going through the tests 1 by one and testing each segment makes it 
a lot easier and gives you the build order
"""

class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_element = Element(item)
        new_element.next = self.head
        self.head = new_element
    
    @property
    def size(self):
        size = 0
        current = self.head
        while current:
            current = current.next
            size += 1
        return size
    
    def pop(self):
        if self.head:
            pop_value = self.head.datum
            self.head = self.head.next
            return pop_value
        return None
    
    def is_empty(self):
        return self.size == 0
    
    @classmethod    
    def from_list(cls, lst:list=[]):
        linked_lst = SimpleLinkedList()
        if lst:
            for item in lst[::-1]:
                linked_lst.push(item)
        return linked_lst
    
    def to_list(self):
        lst = []
        next_item = self.head
        while next_item:
            lst.append(next_item.datum)
            next_item = next_item.next
        return lst
    
    def peek(self):
        return self.head.datum if self.head else None
    
    def reverse(self):
        # return SimpleLinkedList.from_list(self.to_list()[::-1])
        
        r_lst = SimpleLinkedList()
        current = self.head
        while current:
            r_lst.push(current.datum)
            current = current.next
        return r_lst

class Element:
    def __init__(self, datum, next_item=None):
        self.datum = datum
        self.next = next_item
    
    def is_tail(self):
        return self.next == None
