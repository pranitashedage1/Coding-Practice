# Given an infinite sized sorted array and an element x, find if x is present in the array or not
arr = [10, 20, 25, 50, 70, 80, 100, 140, 177, 1980, 7000, 7001, 7002, 7003, 7004, 7009, 8000, 80001, 80002, 80006, 90000, 90001, 90002, 9000003]

def binary_search(low, high, arr, key):
    mid = (low + high)//2
    if low > high:
        return -1
    if arr[mid] == key:
        return arr[mid]
    if arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
    b = binary_search(low, high, arr, key)
    return b
    

def find_element(key, arr):
    if arr[0] == key:
        return key
    i = 1
    while arr[i] < key:
        i = i * 2
    print(i//2)
    print(i)
    a = binary_search(i//2, i, arr, key)
    
    return a

c = find_element(178, arr)
print(c)
