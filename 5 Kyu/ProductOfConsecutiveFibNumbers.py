'''
Your function takes an integer (prod) and returns an array/tuple (check the function signature/sample tests for the return type in your language):

if F(n) * F(n+1) = prod:
(F(n), F(n+1), true)
If you do not find two consecutive F(n) verifying F(n) * F(n+1) = prod:
(F(n), F(n+1), false)
where F(n) is the smallest one such as F(n) * F(n+1) > prod.
Examples:
714 ---> (21, 34, true)
--> since F(8) = 21, F(9) = 34 and 714 = 21 * 34

800 --->  (34, 55, false)
--> since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
'''

def product_fib(_prod):
    curr_prod = 1
    fibo = [0, 1]
    last = 1
    if _prod == 0:
        return [fibo[last-1], fibo[last], True]
    
    while True:
        curr_prod = fibo[last-1] * fibo[last]
        fibo.append(fibo[last-1] + fibo[last])
        if curr_prod == _prod:
            return [fibo[last-1], fibo[last], True]
        elif curr_prod > _prod:
            return [fibo[last-1], fibo[last], False]
        last += 1