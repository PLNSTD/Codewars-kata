'''
You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
'''

def get_middle(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 != 0 else s[mid-1:mid+1]