'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''
def is_isogram(string):
    dict = [0] * 26
    for char in string.lower():
        dict[ord(char)-97] += 1
        if dict[ord(char)-97] > 1:
            return False
        
    return True