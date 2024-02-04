# given a sorted and rotated array of distinct elements, and an element x
# find if x is present in the array or not
# arr = [10, 20, 40, 5, 6, 7, 8] - sorted and rotated for 4 times
# arr = [10, 20, 1, 2, 3, 4, 5] - sorted and rotated for 5 times
# arr = [10, 20, 30, 40, 50, 60, 1] - sorted and rotated for 1 time

# arr = [10, 20, 30, 40, 50, 60, 1, 6, 7, 8]
# arr = [10, 0, 1, 2, 4, 5, 7, 9]
# arr = [10, 20, 30, 40, 50, 60, 1]
arr = [10, 30, 50, 70]

def find_pivot(low, high, arr):
    if low > high:
        return high
    mid = (low + high)//2
    if arr[0] <= arr[mid]:
        return find_pivot(mid+1, high, arr)
    if arr[0] > arr[mid]:
        return find_pivot(low, mid-1, arr) 
a = find_pivot(0, len(arr)-1, arr)
print(a)

def binary_search(low, high, arr, key):
    mid = (low + high)//2
    if low > high:
        return -1
    if arr[mid] == key:
        return arr[mid]
    if arr[mid] < key:
        return binary_search(mid+1, high, arr, key)
    else:
        return binary_search(low, mid-1, arr, key)

key = 90
b = binary_search(0, a, arr[0:a+1], key)
if b:
    print("b = ", b)
if not b:
    c = binary_search(a, len(arr)-1, arr[a:], key)
    print("c = ", c)
