# binary search alwyas work on the sorted array

# def binary_serach(a,key):
#     low = 0
#     high = len(a)-1
#     mid = 0
#     while(low<=high):
#         mid = int((low+high)/2)
#         if key == a[mid]:
#             return a[mid]
#         elif key<a[mid]:
#             high = mid-1
#         elif key>a[mid]:
#             low = mid+1
#     return -1

# a1 = [1, 3, 5, 7, 9, 12, 16, 34, 66, 78]
# key = 78

# b = binary_serach(a1, key)
# print(b)


# Binary search using recursion:

def binary_serach(low, high, key, a):
    if low > high:
        return -1
    mid = int(low + ((high-low)/2))
    if key == a[mid]:
        return a[mid]
    elif key < a[mid]:
        return binary_serach(low, mid-1, key, a)
    elif key > a[mid]:
        return binary_serach(mid+1, high, key, a)


a1 = [1, 3, 5, 7, 9, 12, 16, 34, 66, 78]
key1 = 78
b = binary_serach(0, len(a1)-1, key1, a1)
print(b)
