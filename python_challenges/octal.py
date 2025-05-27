"""
Problem: 
Given an octal input string, your program should produce a decimal output. 

Rules & Requirements:
- Treat invalid input as octal 0
- Note that the only valid digits in an octal number are 0-7
- Take in a string and initiate an Octal instance
- Method to_decimal to convert the number to an integer
- Based on test cases, assuming only doing whole numbers 

Data Structure:
- Input: String
- Output: Decimal integer

Notes:
- Can use a collection as an intermediary, so that we can use indicies 
- Strings are iteratble, so may not need a collection 
- We can use the index combined with len(octal) to determine which power 
- Or, we can flip the string and start with the last number 
- And use an accumulator variable to store the result

Algorithm (for to_decimal):
1. Initialize decimal variable to hold the result and set it = 0
    a. Also initialize a multiplication_factor and set it to 1
    b. Note: This factor will increase by x 10 for each digit place
2. Iterate the string octal starting from the last digit place
3. Multiply the integer transformation of that number by the multiplication_factor
4. Increase the multiplication_factor *= 10
5. Return the decimal which should hold the aggregated result
"""

class Octal:
    def __init__(self, octal: str):
        self.octal = self._validate(octal)
    
    def _validate(self, octal: str) -> str:
        if not octal.isdigit():
            return '0'
        if not all(int(num) < 8 for num in octal):
            return '0'
        return octal
    
    def to_decimal(self) -> int:
        decimal = 0
        multiplication_factor = 1
        for num in self.octal[::-1]:
            decimal += int(num) * multiplication_factor
            multiplication_factor *= 8
        return decimal

print(Octal('130').to_decimal()) # 88
print(Octal('2047').to_decimal()) # 1063
print(Octal('7777').to_decimal()) # 4095