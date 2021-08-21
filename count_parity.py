'''
logic : x >> 32
divides the entire 6 bits word into
two 32 bits chunks and then calculate their XOR
after that do the same for 16, 8, 4, 2, 1 bits
in the end return the last bit of the word by
Anding it with the remaining number
'''

def parity(x):
    x ^= x >>32
    x ^= x >> 16
    x ^= x >>8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


print(parity(8212021))

