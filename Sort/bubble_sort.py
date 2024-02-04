# Bubble Sort:
# Time complexity = O(n^2)
a = [20, 10, 5, 15]
b = len(a)
for i in range(b):
    print("i = ", i)
    for j in range(0, b-i-1):
        print("j = ", j)
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    print("===============================")
print(a)
