'''
Description:
Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
'''

def switcheroo(s):
    opposite = {'a': 'b', 'b': 'a'}
    return ''.join([opposite[char] if char == 'a' or char == 'b' else char for char in s])