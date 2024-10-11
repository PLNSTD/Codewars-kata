'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
The next words should be always capitalized.
'''

def to_camel_case(text):
    value = True
    while value:
        index = text.find('-')
        if index != -1:
            text = text[:index] + text[index+1].upper() + text[index+2:]
        else:
            index = text.find('_')
            if index != -1:
                text = text[:index] + text[index+1].upper() + text[index+2:]
            else:
                value = False
    return text