'''
partition the array such that
elements less than pivot appears at the left and
elements greater than pivot appears to the right
arr = [0,1,2,0,2,1,1]
'''
# this is the brute force apporach

def dutch_national_flag(arr, pivot):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
    for i in reversed(range(len(arr))):
        for j in reversed(range(i)):
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
    return arr
    
    
# this is an efficient apporach

def efficient_apporach(arr, pivot):
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
    larger = len(arr) - 1

    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            break
        elif arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger  -= 1

    return arr

# this is very efficient apoorach

def very_fucking_efficient_apporach(arr, pivot):
    smaller,middle, larger = 0 ,0, len(arr)-1
    while middle < larger:
        if arr[middle] < pivot:
            arr[smaller], arr[middle] = arr[middle], arr[smaller]
            smaller, middle = smaller + 1, middle + 1
        elif arr[middle] == pivot:
            middle += 1
        else:
            arr[middle], arr[larger] = arr[larger], arr[middle]
            larger -= 1
    return arr
