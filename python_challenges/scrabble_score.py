"""
PEDAC

Problem: Write a program that, given a word, compute the Scrabble score for that word.

Letter = Value
A, E, I, O, U, L, N, R, S, T = 1
D, G = 2
B, C, M, P = 3
F, H, V, W, Y = 4
K = 5
J, X = 8
Q, Z = 10

Examples: CABBAGE -> 14
- 3 points for C
- 1 point for each A (there are two)
- 3 points for B (there are two)
- 2 points for G
- 1 point for E

Rules:
- Looks like there's only one case
- Spaces, newlines, etc. don't count 
- Argument passed to class could be in either case 

Data Structure:
- Can keep score map as a dictionary
"""

class Scrabble:
    
    SCORES = {
        ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
        ('D', 'G'): 2,
        ('B', 'C', 'M', 'P'): 3,
        ('F', 'H', 'V', 'W', 'Y'): 4,
        ('K'): 5,
        ('J', 'X'): 8,
        ('Q', 'Z'): 10
    }
    
    def __init__(self, word):
        self.word = word.strip() if word else ''
        
    def single_score(self, letter):
        for letters, score in Scrabble.SCORES.items():
            if letter.upper() in letters:
                return score
        return 0
    
    def score(self):
        total_score = 0
        for letter in self.word.upper():
            total_score += self.single_score(letter)
        return total_score
    
    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()

print(Scrabble('abc').single_score('a'))
print(Scrabble('abc').score())
print(Scrabble.calculate_score(('abc')))

print(Scrabble(None).score())
print(Scrabble.calculate_score((None)))