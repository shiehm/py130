"""
PEDAC

Problem: Find the longest sentence in a string, and the number of words in it. 

Questions:
- Is punctuation (like commas) considered a word? According to the definition, 
it seems like commas are not considered a separate word (just whatever is 
separated by spaces)

Data Structures: Can use list to store separate sentences, then use a dictionary
to store the length if needed
- Input: String (of sentences combined)
- Output: String (1 sentence) and an integer

Algorithm:
1. Identify the sentences and split them up into lists
    a. Identify all sentence ending punctuation and store in constant ENDINGS
    b. Split the string based on ENDINGS (end up with a list of string sentences)
        i. Initialize empty list and holder variable and iterate through the string
        ii. Add each char until you hit an ENDING
        iii. Once you hit an ending, 
            - add the ENDING to the holder 
            - append the holder to the list
            - reset the holder to ''
    c. Split any whitespaces before or after the string off 
2a. Iterate through the list of strings:
    a. Initialize a set of tracker variables for "longest_string" and "longest_count"
    b. Count how many words in the string by splitting by ' ' and using len()
    c. Store the longest count and longest string so far in the tracker variables
    d. Return the tracker variables
Alternatively:
2b. Sort the list of strings using len as a key to sort (key=len):
    a. Return index [-1] (reverse=False is default setting)
"""

def find_sentences(string):
    ENDINGS = ['.', '?', '!']
    
    sentences = []
    current_sentence = ''
    for char in string:
        current_sentence += char
        if char in ENDINGS:
            sentences.append(current_sentence)
            current_sentence = ''
    
    clean_sentences = [sentence.strip() for sentence in sentences]
    return clean_sentences

def longest_sentence(string):
    sentences = [sentence.split() for sentence in find_sentences(string)]
    sentences.sort(key=len)
    longest_sentence = ' '.join(sentences[-1])
    longest_count = len(sentences[-1])
    print(longest_sentence)
    print(f'The longest sentence has {longest_count} words.')

long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.