# Binary search - find the left most element

def binary_serach(low, high, key, a):
    if low > high:
        return -1
    mid = int(low + ((high-low)/2))
    if key == a[mid] and (mid == 0 or a[mid-1] != key):
        return mid
    elif key <= a[mid]:
        return binary_serach(low, mid-1, key, a)
    elif key > a[mid]:
        return binary_serach(mid+1, high, key, a)


a1 = [3, 3, 3, 7, 7, 12, 16, 16, 78, 78]
key1 = 7
b = binary_serach(0, len(a1)-1, key1, a1)
print(b)
