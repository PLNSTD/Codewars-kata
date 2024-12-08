'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''

def count(s):
    occ_dict = {}
    for char in s:
        occ_dict[char] = occ_dict.get(char, 0) + 1
    return occ_dict

# Better try with direct assignment as update is inefficient