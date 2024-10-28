def duplicate_encode(word):
    #your code here
    print(word)
    occurrences_dict = {}
    for char in word.lower():
        occurrences_dict[char] = occurrences_dict.get(char, 0) + 1
    
    output = ''
    for char in word.lower():
        if occurrences_dict[char] > 1:
            output += ')'
        else:
            output += '('
            
    return output