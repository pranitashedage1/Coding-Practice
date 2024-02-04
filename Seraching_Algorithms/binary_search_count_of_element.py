# Binary search - count of the element

def binary_right_serach(low, high, key, a):
    if low > high:
        return -1
    mid = int(low + ((high-low)/2))
    if key == a[mid] and (mid == (len(a) - 1)or a[mid+1] != key):
        return mid
    elif key < a[mid]:
        return binary_right_serach(low, mid-1, key, a)
    else:
        return binary_right_serach(mid+1, high, key, a)
    
def binary_left_serach(low, high, key, a):
    if low > high:
        return -1
    mid = int(low + ((high-low)/2))
    if key == a[mid] and (mid == 0 or a[mid-1] != key):
        return mid
    elif key <= a[mid]:
        return binary_left_serach(low, mid-1, key, a)
    elif key > a[mid]:
        return binary_left_serach(mid+1, high, key, a)

def count_of_index(low, high, key, a):
    left = binary_left_serach(low, high, key, a)
    right = binary_right_serach(low, high, key, a)
    if left == -1 or right == -1:
        return -1
    else:
        return  right - left + 1

a1 = [2, 3, 3, 7, 7, 7, 12, 16, 16, 16, 78, 300]
key1 = 3
b = count_of_index(0, len(a1)-1, key1, a1)
print(b)
