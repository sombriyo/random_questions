''''
Arrange the array in the following order
a[0] <= a[1] >= a[2] <= a[3] >= a[4]...
'''

def arrange(arr):
    '''
    Complexity
    time O(1)
    space O(n)
    '''
     arr = sorted(arr)
     for i in range(len(arr)):
         if i%2 != 0 :
             arr[i], arr[i+1] = arr[i+1], arr[i]

     return arr

def rearrange(arr):
    '''
    Complexity
    time O(1)
    space O(n)
    '''
    for i in range(len(arr)):
        arr[i:i+2] = sorted(arr[i:i+2], reverse= i%2)
    return arr


arr  = [2,1,4,5,6,3,6,7,8]

print(rearrange(arr))
