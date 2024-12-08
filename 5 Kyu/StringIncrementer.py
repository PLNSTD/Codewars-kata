'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

def increment_string(strng):
    first_num_idx = len(strng) - 1 # Start from lastchar
    check_flag = False # Check if there was a digit
    
    # Check if lastchar is digit
    while first_num_idx >= 0 and strng[first_num_idx].isdigit():
        check_flag = True # Encountered digit
        first_num_idx -= 1 # Update lastchar
    
    # If there was not a single digit return input_string+'1' -> input_string1
    if not check_flag:
        return strng + '1'
    
    # Adjust idx to num since idx was set to a non-digit
    first_num_idx += 1
    
    # Get num incremented and then casted to string
    str_num = str(int(strng[first_num_idx:]) + 1)
    
    # Get total num of digits -> difference between the length of the string and the idx of first digit
    padding = len(strng) - first_num_idx
    
    # Return string without digits + the real number padded with zeros -> 
    # input_strng0099 (real_num: 99, incremented: 100) = output_strng0100
    return strng[:first_num_idx] + str_num.zfill(padding)