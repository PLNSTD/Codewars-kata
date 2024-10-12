'''
Complete the solution so that the function will break up camel casing, using a space between words.
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''

def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

# OR

def solution(s):
    output = ''
    for i in s:
        if ord(i) < 97:
            output += ' '
        output += i
    return output