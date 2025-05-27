"""
Problem: 
Write a program that will take a string of digits 
and return all the possible consecutive number series 
of a specified length in that string.

Examples:
- For example, the string "01234" has the following 3-digit series:
    - 012
    - 123
    - 234

Requirements:
- Looks like the class is initialized with 1 string argument of digits
- And there is a "slices" method that gives all possible strings of that length

Data Structure:
- From the test cases it looks like the return slices are contained in lists 
- With each digit separate 

Notes:
- We can use index slicing
- Given a certain length (validate it)
- start from index 0 until that length (since end is excl. can use in slice)
    - initialize a return variable as an empty list 
    - initialize the current_start at 0
    - slice will be current_start to current_start + length
- keep adding 1 to the current_start UNTIL current_start + given length = 
the length of the digit-string

Algorithm (for slices): 
Given the length of each slice, find all the consecutive strings of that length 
within the total string
1. Initialize a results list
2. Initialize a start variable and set it to 0 
3. Iterate taking a slice from start to start + length
4. Stop the iteration when start + length > length of the string
5. Turn each resultant string of digits into a list of integers before 
appending to reuslts
6. Return results
"""

class Series:
    def __init__(self, string):
        self.string = self._validate(string)
    
    def _validate(self, string):
        if not isinstance(string, str):
            raise TypeError('Input needs to be a string')
        if not string.isdigit():
            raise ValueError('String must only contain digits')
        return string
        
    def slices(self, length):
        if length > len(self.string) or length < 1:
            raise ValueError(f'Length must be a positive value <= {len(self.string)}')
        
        results = []
        start = 0
        while start + length <= len(self.string):
            str_slice = self.string[start:start + length]
            int_slice = [int(num) for num in str_slice]
            results.append(int_slice)
            start += 1
        
        return results

# series = Series("01234")
# print(series.slices(1))
# print(series.slices(3))
# print(series.slices(5))