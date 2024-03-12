# find distict elements from the array
# arr = [1, 2, 1, 3, 10, 20, 1, 2, 3]
# o/p = 5


arr = [1, 2, 1, 3, 10, 20, 1, 2, 3]
# arr = [1, 1, 1, 1, 1, 1, 1]
s1 = set()
for i in arr:
    s1.add(i)
print(len(s1))

