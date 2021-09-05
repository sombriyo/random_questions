''''
write a program that takes and integer
and return all the primes upto that integer
'''

import time

def generate_primes(num):
    '''
    The logic here is to sieve out the multiples of the
    number starting from 2 till the number -> num
    so that we can find out effectively which are the prime numbers
    time complexity = O(nloglog(n))
    space = O(n^2)
    '''
    primes = []
    is_prime = [False, False] + [True] * (num-1)
    for i in range(2, num + 1):
        if is_prime[i]:
            primes.append(i)

        # sieving out the multiples
        for i in range(i, num + 1, i):
            is_prime[i]  = False

    return primes


def generate_primes_2(num):
    if num <2 :
        return []
    size = (num - 3) // 2 + 1
    primes = [2]
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = 2 *i +3
            primes.append(p)
            # sieving( finding the multiples) of  p^2 instead of P
            # which would be (2*(i**2) + 6 *i + 3)
            for j in range((2*(i**2) + 6 *i + 3), size, p):
                is_prime[j] = False
    return primes


start = time.time()
num = 1234567
x = generate_primes_2(num)
print(x)
end = time.time()
print(end - start)


