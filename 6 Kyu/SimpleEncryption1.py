'''Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.'''

def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    
    for i in range(n):
        half_index = len(encrypted_text) // 2
        left_text = encrypted_text[:half_index]
        right_text = encrypted_text[half_index + 1:]
        text = encrypted_text[half_index]
        left_idx = 0
        right_idx = 0
        
        while left_idx < len(left_text) and right_idx < len(right_text):
            text += left_text[left_idx] + right_text[right_idx]
            left_idx += 1
            right_idx += 1

        while left_idx < len(left_text):
            text += left_text[left_idx]
            left_idx += 1
        while right_idx < len(right_text):
            text += right_text[right_idx]
            right_idx += 1
            
        encrypted_text = text
    return encrypted_text

def encrypt(text, n): 
    for i in range(n):
        odd_text, even_text = '',''

        for index in range(len(text)):
            if index % 2 == 0:
                even_text += text[index]
            else:
                odd_text += text[index]

        text = odd_text + even_text
    return text