''''
calculate power using bitwise operator
'''

def brute_force(x,y):
    ''''
    Here the logic is simple
    repeated multiplications of x
    '''
    ans = 1
    while y:
        ans *= x
        y -= 1
    return ans

def efficient_apporach(x,y):
    '''
    Here the logic is simple
    we have to multiply x = x^2, then x^4, x^8...
    and at the same time just reduce the value of power i.e. y
    by half.
    '''
    result = 1
    if y < 0:
        x , y = 1/x, -y
    while y:
        if y &1:
            result *= x
        x, y = x *x, y >> 1
    return result



a = 3
b = 123456
#one = brute_force(a,b)
two = efficient_apporach(a,b)
print(len(str(two)))
#print(f'The output using brute force approach is : {one}')
print(f'The output using Efficient approach is : {two}')
