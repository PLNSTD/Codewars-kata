'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''

def count(s):
    dict = {}
    for char in s:
        dict.update({char: 1 if dict.get(char) == None else dict.get(char) + 1})
    return dict

# Better try with direct assignment as update is inefficient