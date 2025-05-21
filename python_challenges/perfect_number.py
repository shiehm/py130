"""
PEDAC
Problem: Categorize numbers as perfect, abundant, or deficient based on its 
Aliquot sum: the sum of a number's positive divisors (no remainder).
- Perfect numbers have an Aliquot sum that is equal to the original number.
- Abundant numbers have an Aliquot sum that is greater than the original number.
- Deficient numbers have an Aliquot sum that is less than the original number.

Examples:
6 is a perfect number since its divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.
28 is a perfect number since its divisors are 1, 2, 4, 7, and 14 and 1 + 2 + 4 + 7 + 14 = 28.
15 is a deficient number since its divisors are 1, 3, and 5 and 1 + 3 + 5 = 9 which is less than 15.
24 is an abundant number since its divisors are 1, 2, 3, 4, 6, 8, and 12 and 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36 which is greater than 24.
Prime numbers 7, 13, etc. are always deficient since their only divisor is 1.

Data Structures:
- Will need a collection like a list to store the divisors

Algorithm:
- Class will take in an integer as an argument, and have the following methods:
- Find all the divisors of a number 
    - Could do this iteratively but that would take a long time if the number is huge 
    - Then sum the divisors 
- classify -> categorize the result
"""

class PerfectNumber:
    def __init__(self, number: int):
        self.number = PerfectNumber.validate(number)
        self.divisors = PerfectNumber.find_divisors(number)
        self.aliquot = PerfectNumber.aliquot_sum(number)
        self.category = PerfectNumber.classify(number)
    
    @classmethod
    def validate(cls, number):
        if number < 0:
            raise ValueError('Input must be a positive integer')
        return number
    
    @classmethod
    def find_divisors(cls, number):
        divisors = [1]
        for i in range(2, number):
            if number % i == 0:
                divisors.append(i)
        return divisors
    
    @classmethod
    def aliquot_sum(cls, number):
        divisors = cls.find_divisors(number)
        return sum(divisors)
    
    @classmethod
    def classify(cls, number):
        valid_num = cls.validate(number)
        aliquot_sum = cls.aliquot_sum(valid_num)
        if aliquot_sum == number:
            return 'perfect'
        elif aliquot_sum > number:
            return 'abundant'
        else:
            return 'deficient'
    

print(PerfectNumber.classify(13))
print(PerfectNumber.classify(28))
print(PerfectNumber.classify(12))
# print(PerfectNumber.classify(-1))