'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''

def rot13(message):
    alphabet = []
    for i in range(26):
        alphabet.append(chr(ord('a') + i))
        
    ciphered = ''
    for char in message:
        if ord(char) >= ord('A') and ord(char) <= ord('Z'): 
            ciphered_char_idx = ord(char) - ord('A') + 13
            if ciphered_char_idx >= 26:
                ciphered_char_idx = ciphered_char_idx - 26
            ciphered += alphabet[ciphered_char_idx].upper()
        elif ord(char) >= ord('a') and ord(char) <= ord('z'):
            ciphered_char_idx = ord(char) - ord('a') + 13
            if ciphered_char_idx >= 26:
                ciphered_char_idx = ciphered_char_idx - 26
            ciphered += alphabet[ciphered_char_idx]
        else:
            ciphered += char
    
    return ciphered