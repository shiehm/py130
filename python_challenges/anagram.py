"""
PEDAC

Problem: Write a program that 
- takes a word and a list of possible anagrams and 
- selects the correct sub-list that contains the anagrams of the word.

Example: 
- given the word "listen" and 
- a list of candidates like "enlists", "google", "inlets", and "banana"
- return a list containing "inlets"

Data Structure:
- We need a match method
- which will return a list of anagrams 

Rules:
- Looks like case doesn't matter
- Each letter has to be used precisely once
- Can't return the same word 
- No clear requirements on order so not going to worry about that 

Issues:
- We need a way to track the letters
- So can have a tracker string, and each time a letter matches reduce it 
- If the matcher string == '' at the end, append the anagram to the list 

Create a helper function that sees if one individual word is an anagram:
- Take the possible anagram as an argument
- Set a tracker variable = list(word)
- iterate through the word, if it matches, remove the letter from the list(word)
- if the len(tracker) == 0, return True
- add an edge case -> If the word == the word then return false
- and if the words are different lengths, then it won't be == 

Algorithm (for match):
- Take the list of possible anagrams as an argument
- Initialize and assign a results variable `anagrams` = []
- Iterate through the possible anagrams word by word
- Feed word into helper function, if true then append to `anagrams`
- return `anagrams`
"""

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def single_match(self, word):
        length_check = len(word) != len(self.word)
        word_check = word.casefold() == self.word.casefold()
        if length_check or word_check:
            return False
        tracker = [item.casefold() for item in list(word)]
        for char in self.word:
            if char.casefold() in tracker:
                tracker.remove(char.casefold())
        return not tracker
    
    def match(self, lst):
        anagrams = []
        for item in lst:
            if self.single_match(item):
                anagrams.append(item)
        return anagrams

# anagram = Anagram('hello')
# print(anagram.match(['hel', 'ji', 'llo', 'elloh', 'lohel']))

good = Anagram('good')
print(good.match(['dog']))
