'''
Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.

Examples
Program "iiisdoso" should return numbers [8, 64].
Program "iiisdosodddddiso" should return numbers [8, 64, 3600].
'''

def parse(data):
    
    output = []
    
    # Each command will have its function
    commands = {
        'i': lambda a: a + 1,
        'd': lambda a: a - 1,
        's': lambda a: a ** 2,
        'o': lambda a: output.append(a) or a
    }
    
    curr_num = 0
    
    for command in data:
        if command in 'idso': # Check if command is valid
            curr_num = commands[command](curr_num)

    return output