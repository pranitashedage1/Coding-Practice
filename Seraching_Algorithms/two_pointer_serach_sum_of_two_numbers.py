# Given an sorted array and a number x, we need to find if there is a pair in the array with sum equals to x

# arr = [2, 5, 8, 12, 30]
# key = 17
# O/p should be Yes, as 12 + 5 = 17

def find_sum(start, end, arr, key):
    if start >= end:
        return False
    if arr[start] + arr[end] == key:
        return True
    elif arr[start] + arr[end] > key:
        return find_sum(start, end-1, arr, key)
    else:
        return find_sum(start+1, end, arr, key)



arr = [2, 5, 8, 12, 30]
key = 10

a = find_sum(0, len(arr)-1, arr, key)
print(a)