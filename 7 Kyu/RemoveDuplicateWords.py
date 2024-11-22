'''
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
'''

def remove_duplicate_words(s):
    my_dict = {}
    for word in s.split():
        my_dict[word] = 1
    return ' '.join(my_dict.keys())