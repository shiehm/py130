"""
Prioblem:
- Write a program to determine whether a triangle is equilateral, isosceles, or scalene.

Requirements:
- An equilateral triangle has all three sides the same length.
- An isosceles triangle has exactly two sides of the same length.
- A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, 
- all sides must be of length > 0, 
- and the sum of the lengths of any two sides must be > the third side.

Algorithm:
1. Test if the object is a triangle using the parameters above 
"""

class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self.is_triangle:
            raise ValueError('Not a triangle')
    
    @property
    def is_triangle(self):
        has_length = all([side > 0 for side in self.sides])
        two_gt_one = all([side < sum(self.sides) - side for side in self.sides])
        not_negative = not any([side < 0 for side in self.sides])
        return has_length and two_gt_one and not_negative
    
    @property
    def kind(self):
        if len(set(self.sides)) == 1:
            return "equilateral"
        elif len(set(self.sides)) == 2:
            return "isosceles"
        else:
            return "scalene"

    def __str__(self):
        return f'{self.kind} triangle'
        

print(Triangle(2,2,2))
print(Triangle(1,2,2))
print(Triangle(2,3,4))
try:
    print(Triangle(0, 3, 2))
except ValueError as e:
    print(f'{e}')