'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(st):
    my_alphabet_occ = {}
    for char in range(ord('a'), ord('z')+1):
        my_alphabet_occ[char] = 0
        print(char)
        
    for char in st:
        if char.isalpha():
            my_alphabet_occ[ord(char.lower())] = 1
    
    for key in my_alphabet_occ:
        if my_alphabet_occ[key] == 0:
            return False
    
    return True