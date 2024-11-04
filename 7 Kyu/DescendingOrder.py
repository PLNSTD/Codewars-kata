'''
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
'''

def descending_order(num):
    my_list = []
    while num > 0:
        my_list.append(num % 10)
        num = num // 10
    my_list.sort(reverse=True)
    
    output = 0
    
    for i in range(len(my_list) - 1, -1, -1):
        output += my_list[i] * pow(10,len(my_list)-i-1)
        
    return output