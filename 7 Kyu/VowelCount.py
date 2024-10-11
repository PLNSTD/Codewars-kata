'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def get_count(sentence):
    return sum(1 for let in sentence if let in 'aeiou')

# def get_count(sentence):
#     cnt = 0
#     for i in sentence:
#         if i in 'aeiou':
#             cnt += 1
#     return cnt

# def get_count(sentence):
#     occurrences = [1 for vowel in sentence if vowel in 'aeiou']
#     return occurrences.count(1)