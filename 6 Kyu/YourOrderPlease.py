'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''

def order(sentence):
    sorted_sentence = {}
    final_sentence = ''
    
    for word in sentence.split(): # [is2, Thi1s, T4est, 3a] length = 4
        for char in word: # is2 -> [i, s, 2] 
            if char >= '1' and char <= '9':
                position = int(char)
                sorted_sentence[position] = word
                
    ''' sorted_sentence = {
        2: 'is2'
        1: 'Thi1s'
        4: 'T4est'
        3: '3a'
    }'''
    
    total_words = len(sentence.split())
    
    for position in range(total_words): # 0,1,2,3 -> You want: 1 to 4 (postition + 1)
        final_sentence = final_sentence + sorted_sentence[position + 1]
        
        if position < total_words - 1:
            final_sentence += ' '
            
    
    return final_sentence