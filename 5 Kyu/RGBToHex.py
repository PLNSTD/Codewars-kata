'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
'''

def rgb(r, g, b):    
    hex_color = ''
    for color in [r, g, b]:
        if color < 0:
            color = 0
        elif color > 255:
            color = 255
        first_hex = color // 16
        second_hex = color % 16
        hex_color += digit_to_hex(first_hex)
        hex_color += digit_to_hex(second_hex)
    return hex_color

def digit_to_hex(x):
    hex_characters = ['A','B','C','D','E','F']
    
    if x > 9:
        return hex_characters[x - 10]
        
    return str(x)