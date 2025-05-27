"""
Problem:
The diamond exercise takes as its input a letter, and outputs it in a 
diamond shape. Given a letter, it prints a diamond starting with 'A', 
with the supplied letter at the widest point.

Notes:
- Each "row" is going to have an odd number of spaces + char places 
    - The length//2 is going to be the index position of the middle char 
    - 'A' will always occupy that 
    - Then 'B' will be + and - 1 space from middle char 
    - We can use chr() and ord() to iterate letter positioning 
- We can use the places of alphabet as a frame of reference
- All rows will have a total length the size of the widest row 
- Each row length until the widest goes up by 2 starting from 1 
- Each row will have an odd number of spaces holding the letter
- Then spaces will fill the left and right sides
- And it will end with a newline '\n'
- If we get half the diamond, we can just reverse it [1::-1] to get other half

Thinking it through:
- 'A' will be 'A' plus a newline, that's it
- 'B' will be 'B' then a space plus 'B'
- 'C' will be 'C' then 3 spaces plus 'C'
- 'D' will be 'D' then 5 spaces plus 'D'
- We can have something that automatically increments existing lines with 
1 space on either end for each letter added... 
OR
- We can start with the deepest line. 
- Then create the next line and add it both before and after in the list 
- And keep going until we get to 'A'

Requirements:
- Cases don't seem to matter but the arguments are all capital in the examples
- There seems to be just 1 classmethod needed
- The number of rows will = number of spaces length wise at the widest

Algorithm: 
1. Figure out the dimensions (it will be a square except + newlines at row ends)
    a. Take the number of places separating the letter from 'A' using ord
    b. Use that to determine max number of spaces/rows with ea consecutive
    letter having 2 more spaces vs. 'A' (which has 1)
    c. Use indexing on a range to get the number of spaces for length / rows
2. Starting with the letter passed as an argument (the widest line) 
    a. Initialize a left_index set at 0
    b. Initialize a right_index set at dimensions - 1 
    c. Initialize the current_row with [' '] * dimensions
    d. Fill in the current letter at left and right indicies
    e. Move the left index up by 1, right index down by 1 
    f. Decrement the letter by 1 (i.e. go backwards until you hit 'A')
    g. Keep going until left == right index which should be at 'A'
"""

class Diamond:
    @classmethod
    def _validate(cls, letter):
        if not isinstance(letter, str):
            raise TypeError('Argument needs to be a string between A-Z')
        
        capital_letters = [chr(ord_num) for ord_num in range(ord('A'), ord('Z') + 1)]
        if letter not in capital_letters:
            raise ValueError('Argument needs to be a capital letter from A-Z')
        
        return letter
        
    @classmethod
    def make_diamond(cls, letter):
        letter = cls._validate(letter)
        
        position = ord(letter) - ord('A')
        width = 2 * position + 1
        mid_point = width // 2
        # end_range = 26 * 2 + 1 # 26 letters, 2 spaces each after 'A' which has 1
        # dimensions = range(1, end_range, 2)[position] # number of rows and spaces
        # mid_point = dimensions // 2
        
        results = []
        current_ord = ord(letter)        
        left_index = 0
        right_index = width - 1
        while left_index != right_index:
            current_row = [' '] * width
            current_row[left_index] = chr(current_ord)
            current_row[right_index] = chr(current_ord)
            
            left_index += 1
            right_index -= 1
            current_ord -= 1
            
            results.append(''.join(current_row) + '\n')
        
        current_row = [' '] * width
        current_row[mid_point] = 'A'
        results.append(''.join(current_row) + '\n')
        
        return ''.join(results[::-1] + results[1:])

# print(Diamond.make_diamond('A'))        
# print(Diamond.make_diamond('B'))
# print(Diamond.make_diamond('C'))
# print(Diamond.make_diamond('Z'))
# print(Diamond.make_diamond('a'))
# print(Diamond.make_diamond(1))