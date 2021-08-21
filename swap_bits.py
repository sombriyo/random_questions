'''
a program that can swap bits
logic: the logic is simple
swap the bits = filpping the bits from 1-0 and from 0-1
Time complexity - O(1)
space Complexity - O(1)
'''

def swap_bits(x, i, j):
    if (x >> i & 1) != (x >> j & 1):
        bit_mask = 1<< i | 1 <<j
        x ^= bit_mask
    return x


print(swap_bits(10,2,3))
