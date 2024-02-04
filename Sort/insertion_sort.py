# Insertion Sort
# Time complexity = O(n^2)
a = [4, 9, 3, 6, 2]
b = len(a)
for i in range(1, b):
    j = i
    while a[j-1] > a[j] and j > 0:
        a[j-1], a[j] = a[j], a[j-1]
        j -= 1
print(a)
