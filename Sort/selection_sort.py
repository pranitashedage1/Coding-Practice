# selection Sort
# Time complexity = O(n^2)
a = [4, 9, 3, 6, 2]
b = len(a)
for i in range(b):
    min_index = i

    for j in range(i+1, b):
        if min_index > a[j]:
            min_index = a[j]
    a[i], a[min_index] = a[min_index], a[i]
