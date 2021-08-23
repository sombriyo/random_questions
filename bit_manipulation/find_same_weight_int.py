'''
The question is to find the integer with closest weight
here weight mean by number of ones in the binary form of the integer
1. n should not equal to y
2. And the difference |y-n| should me minimum
'''

def find_closest_weight(n):
    bits = 64
    for i in range(bits):
        if (n >> i) & 1 != (n >> (i+1)) & 1:
            n ^= (1 << i) | ( 1<<(i+1))
            return n


print(find_closest_weight(7
                          ))
