"""
Problem: Create a custom implementation of set 

Data Structure: List (try again later using Dictionary)
"""

class CustomSet:
    def __init__(self, collection=None):
        if collection is None:
            collection = []
        
        set = []
        for item in collection:
            if item not in set:
                set.append(item)
        self.set = sorted(set)
    
    def is_empty(self):
        return not self.set
    
    def contains(self, other):
        return other in self.set
    
    def is_subset(self, other):
        self._class_validator(other)
        for item in self.set:
            if item not in other.set:
                return False
        return True
    
    def is_disjoint(self, other):
        self._class_validator(other)
        for item in self.set:
            if item in other.set:
                return False
        return True
    
    def is_same(self, other):
        self._class_validator(other)
        return sorted(other.set) == sorted(self.set)
    
    def add(self, item):
        if item not in self.set:
            self.set.append(item)
            self.set.sort()
    
    def intersection(self, other):
        self._class_validator(other)
        
        intersection = CustomSet()
        for item in self.set + other.set:
            if item in self.set and item in other.set and item not in intersection.set:
                intersection.add(item)
        return intersection
    
    def difference(self, other):
        self._class_validator(other)
        
        difference = CustomSet()
        for item in self.set:
            if item not in other.set and item not in difference.set:
                difference.add(item)
        return difference
    
    def union(self, other):
        self._class_validator(other)
        
        union = CustomSet(self.set)
        for item in other.set:
            if item not in union.set:
                union.add(item)
        return union
    
    def _class_validator(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
    
    def __str__(self):
        return f'{self.set}'
        
    def __eq__(self, other):
        return self.is_same(other)
