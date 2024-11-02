'''
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]

# TOP-DOWN
def tower_builder(n_floors):
    tower = []
    for floor in range(n_floors):
        white_spaces = ' ' * (n_floors - floor - 1)
        block = '*'
        n_blocks = 2 * floor
        tower.append(white_spaces + block + (block*n_blocks) + white_spaces)
        print(white_spaces + block + (block*n_blocks) + white_spaces)
    return tower'''

# BOTTOM-UP
def tower_builder(n_floors):
    tower = []
    base_blocks = '*' + ('*' * 2 * (n_floors - 1))
    white_spaces = ''
    for floor in range(n_floors):
        base = white_spaces + base_blocks + white_spaces 
        tower.insert(0, base)
        white_spaces += ' '
        base_blocks = base_blocks[:-2]
    return tower