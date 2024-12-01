'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''

def zero(inner = None): return 0 if inner is None else inner(0)  #your code here
def one(inner = None): return 1 if inner is None else inner(1) #your code here
def two(inner = None): return 2 if inner is None else inner(2) #your code here
def three(inner = None): return 3 if inner is None else inner(3) #your code here
def four(inner = None): return 4 if inner is None else inner(4) #your code here
def five(inner = None): return 5 if inner is None else inner(5) #your code here
def six(inner = None): return 6 if inner is None else inner(6) #your code here
def seven(inner = None): return 7 if inner is None else inner(7) #your code here
def eight(inner = None): return 8 if inner is None else inner(8) #your code here
def nine(inner = None): return 9 if inner is None else inner(9) #your code here

def plus(b): return lambda a : a + b
def minus(b): return lambda a : a - b
def times(b): return lambda a : a * b
def divided_by(b): return lambda a : a // b