'''
Divide two number without using / operator
'''

import numpy as np

def brute_force(x, y):
    '''
    This will calculate x / y
    '''
    div = 0.0
    if x > y:
        a = x
        b = y
    elif x < y:
        a = y
        b = x
    while a >= b:
        a -= b
        div += 1
    if x < y:
        div = np.reciprocal(div)
    return div, a


def efficient_apporach(x, y):
    '''
    This has complexity of log(n)
    First we found the highest number that is lower than y,
    then substract this number from y and update x as the result of substraction
    at the same time add the lowest power of 2 in the result.
    '''
    result , power = 0, 32
    #finding the highest number 
    k = y << power
    while x >= y:
        while k > x:
            k >>= 1
            power -= 1
        result += 1 << power

        x -= k
    return result, x

x = 11
y = 2
a, b =brute_force(x, y)
c, d = efficient_apporach(x, y)
print(f'By Brute force approach the quotient is {a}, and the remainder is {b}')
print(f'By efficient approach the quotient is {c}, and the remainder is {d}')



