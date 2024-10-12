'''
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
'''
def solution(s):
    output = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        output.append(s[i:i+2])
    return output

def solution(s):
    output = []
    new_pair = ''
    for i in range(len(s)):
        if i == 0 or i % 2 == 0:
            new_pair = s[i]
        else:
            new_pair += s[i]
            output.append(new_pair)
            new_pair = ''
    if len(new_pair) > 0:
        new_pair += '_'
        output.append(new_pair)
    return output