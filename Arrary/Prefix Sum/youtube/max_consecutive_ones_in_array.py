# maximum coxecutive ones in the array -
# arr = [0, 1, 1, 0, 0, 1, 1, 1, 0]
# o/p = 3, as maximum consecutive ones are 3

# arr = [1, 1, 0, 1]
# o/p = 2

# arr = [1, 1, 1, 1, 1]
# o/p = 5

# arr = [0, 0, 0]
#  o/p = 0

# Naive approach - This hac complexicity O(n2)

# arr =  [0, 0, 0]
# n = len(arr)
# maxCount = 0
# for i in range(n):
#     count = 0
#     for j in range(i, n):
#         if arr[j] == 1:
#             count += 1
#         else:
#             break
#     if count > maxCount:
#         maxCount = count

# print(maxCount)

# Effective Approach - O(n)
arr = [0, 0, 0]
count = 0
maxCount = 0
for i in arr:
    if i == 1:
        count += 1
    else:
        count = 0
    maxCount = max(count, maxCount)
print(maxCount)
