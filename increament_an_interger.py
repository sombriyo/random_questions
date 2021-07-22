'''
Increament the interger.
A simple apporach is to merge a list then
then increment the number and after that
split the list, but in some languages there is a 
limit of an integer.
Another efficient apporach is to use elementary addition 
in which we increase the least significant digit and raise propagate the carry

TC- O(n), sc - O(1)
'''
def plusone(a):
    for i in reversed(range(1, len(a))):
        if a[i] != 10:
            break
        a[i] = 0
        a[i-1] += 1
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a
