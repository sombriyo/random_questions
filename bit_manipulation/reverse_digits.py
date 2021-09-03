'''
Reverse the digits of a number
The logic here is to convert the interger into string 
then carry out reverse operations.
complexity : O(1)
'''

def reverse_digits(a):
    if a < 0:
        a = -1*a
        a = int(str(a)[::-1])
        return a*-1
    else:
        a = int(str(a)[::-1])
        return a


a = 123456789
b = reverse_digits(a)
print(f'The reverse of the digits are : {b}')
