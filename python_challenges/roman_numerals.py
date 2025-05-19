"""
Notes:
- The best way to do this is to get the base10 amounts first 
    - i.e. how many 1000s, 100s, 10s etc.
- Then convert those into roman numerals
    - This prevents the 5s (D, L, V) from messing up the conversion
- Instead of building a get_base10 function... I can just split the numbers into 
  places (and insert 0 before)! It's already in base10! 
    - But then I'd need to insert 0s before
- Conversion to roman numerals is the hard part
    - I could make everything in the tens place first (M, C, X, I) and then take
    the result and "simplify" it with the halfway and next ten
    - So IIIIIIIII -> IX, IIII -> IV

Algorithm for converting to romans:
1. For powers of ten in 1000, 100, 10, 1 find out how many are in the num
    - Example: 1204 -> 1 x 1000, 2 x 100, 0 x 10, 4 x 1
    - Example: 93 -> 0 x 1000, 0 x 100, 9 x 10, 3 x 1
    - Example: 141 -> 0 x 1000, 1 x 100, 4 x 10, 1 x 1
2. The going from lower to highest, convert those into roman numerals
    - 1204: 1s -> IV, 10s -> _, 100s -> CC, 1000s -> M = MCCIV
    - 93: 1s -> III, 10s -> XC, 100s -> _, 1000s -> _ = XCIII
    - 141: 1s -> I, 10s -> XL, 100s -> C, 1000s -> _ = CXLI
    - The algorith here seems to be 
        - up to 3, just 1-3 x the roman
        - 4 or 9, roman + halfway, roman + next_ten
        - 5-8, halfway + (6-8) 1-3 x roman 
        
    ROMAN = {
        1000: 'M',
        500: 'D',
        100: 'C', 
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }
"""

class RomanNumeral:
    def __init__(self, num):
        self.num = num
        
    def to_roman(self):
        def get_base10(num):
            tens_places = [int(x) for x in list(str(num))]
            if len(tens_places) < 4:
                for _ in range(4 - len(tens_places)):
                    tens_places.insert(0, 0)
            return tens_places
        
        def convert(num):
            tens = get_base10(num)[::-1]
            roman_tens = ['I', 'X', 'C', 'M']
            roman_halves = ['V', 'L', 'D']
            results = []
            for i in range(3):
                if tens[i] == 9:
                    results.append(roman_tens[i] + roman_tens[i + 1])
                elif tens[i] >= 5:
                    results.append(roman_halves[i] + (tens[i] - 5) * roman_tens[i])
                elif tens[i] == 4:
                    results.append(roman_tens[i] + roman_halves[i])
                else:
                    results.append(roman_tens[i] * tens[i])
                    
            results.append('M' * tens[3])
            return ''.join(results[::-1])
                    
        return convert(self.num)
        
print(RomanNumeral(1204).to_roman())
print(RomanNumeral(93).to_roman())
print(RomanNumeral(141).to_roman())
print(RomanNumeral(336).to_roman())
print(RomanNumeral(2876).to_roman())
