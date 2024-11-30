'''
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
'''

def solution(string):
    return ''.join([string[idx] for idx in range(len(string)-1, -1, -1)])