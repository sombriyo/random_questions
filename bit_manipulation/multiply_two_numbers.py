'''
Multiply two number using
Bitwise operator
'''

def brute_force(a,b):
    '''
    The logic here is simple just
    increase the first number second number times
    '''
    mul = 0
    while a:
        mul += b
        a -= 1
    return mul


def russian_peasant_method(a,b):
    '''
    The logic here is to double a number
    and half the second number and keep adding it
    till the second number become 1
    '''
    res = 0
    while b:
        if b & 1:
            res += a

        a <<= 1
        b >>= 1
    return res

a =russian_peasant_method(10,20)
b = brute_force(10,20)
print(f'By brute force approach the answer is : {b}','\n'
      f'and By Russian Peasant method the answer is :{a}')






