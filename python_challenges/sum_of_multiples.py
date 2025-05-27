"""

Problem:
- Given a natural number and a set of one or more other numbers default: {3, 5}
- find the sum of all the multiples of the numbers in the set < first number

Example:
- if we list all the natural numbers up to, but not including, 20 that are 
multiples of either 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18
- The sum of these multiples is 78.

Notes:
- Takes in 2 arguments: 
    - a natural number (positive integer)
    - a set of multiples (default 3, 5)
- Need a validation method
- Need to create a results set
- Can use range to get all the multiples for each number in multiples set
    - And then merge the sets (use union |)

Data Structure:
- Using set is best so that we don't have duplicates
- We can use range to create the multiples

Algorithm:
sum_up_to
1. Taking the set of multiples (or default set):
    - Initialize a results set
        a. For each number in the set,
        b. Take the range(0, number, multiple)
        c. Add that to the results set 
    
"""

class SumOfMultiples:
    def __init__(self, *multiples):
        if not multiples:
            multiples = {3, 5}
        self.multiples = set(self._validate(num) for num in multiples)
    
    def _validate(self, number):
        if number < 1 or number % 1 != 0:
            raise ValueError('Needs to be a natural number')
        return number
    
    def to(self, number):
        number = self._validate(number)
        results = set()
        for multiple in self.multiples:
            current_set = set(range(multiple, number, multiple))
            results.update(current_set)
        return sum(results)
    
    @classmethod
    def sum_up_to(cls, number):
        return SumOfMultiples().to(number)
    

# print(SumOfMultiples().sum_up_to(10)) #23
# print(SumOfMultiples().sum_up_to(100)) # 2,318
# print(SumOfMultiples().sum_up_to(1000)) #233,168

# print(SumOfMultiples.sum_up_to(10)) #23
# print(SumOfMultiples.sum_up_to(100)) # 2,318
# print(SumOfMultiples.sum_up_to(1000)) #233,168

# print(SumOfMultiples().to(10)) #23
# print(SumOfMultiples().to(100)) # 2,318
# print(SumOfMultiples().to(1000)) #233,168