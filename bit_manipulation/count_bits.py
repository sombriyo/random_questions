'''
a simple program to count bits of an
binary number
x -> 10(1010)


'''


def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x &1
        x >>= 1
    return num_bits

def count_parity(x):
    '''
    brute force apporach
    :param x:
    :return:
    '''
    parity = 0
    while x:
        parity ^= x &1
        x >>= 1
    return parity

def count_parityv2(x):
    '''
    this function drops the lowest set bit
    '''
    parity = 0
    while x:
        parity ^= 1
        x &= x-1
    return parity

print(count_parityv2(10))
