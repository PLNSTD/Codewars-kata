'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''

def rot13(message):
    output = ''
    for char in message:
        if char.isalpha():
            base_letter = ord('a') if char.islower() else ord('A')
            coded_char = chr((ord(char) - base_letter + 13) % 26 + base_letter)
            output += coded_char
        else:
            output += char
    return output