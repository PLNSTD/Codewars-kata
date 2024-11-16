'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
'''

def find_outlier(integers):
    cnt_even, cnt_odd = 0, 0
    even_num = None
    odd_num = None
    for num in integers:
        if num % 2 == 0:
            cnt_even += 1
            if cnt_even == 1:
                even_num = num
        else:
            cnt_odd += 1
            if cnt_odd == 1:
                odd_num = num
    return odd_num if cnt_even > 1 else even_num