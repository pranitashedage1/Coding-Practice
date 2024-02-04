# Given an sorted array and a number x, we need to find if there is a triplet in the array with sum equals to x

# arr = [2, 3, 4, 8, 9, 20, 40]
# key = 32
# O/p should be Yes, as 4 + 8 + 20 = 32

def find_triplet(arr, start, end, key):
    if start >= end:
        return False
    if arr[start] + arr[end] == key:
        return (arr[start] , arr[end], True)
    elif arr[start] + arr[end] > key:
        return find_triplet(arr, start, end-1, key)
    else:
        return find_triplet(arr, start+1, end, key)

arr = [2, 3, 4, 8, 9, 20, 40]
key = 70

n = len(arr)
for i in range(n):
    a = find_triplet(arr, i+1, n-1, key-arr[i])
    if a:
        print(i)
        break
print(a, arr[i])