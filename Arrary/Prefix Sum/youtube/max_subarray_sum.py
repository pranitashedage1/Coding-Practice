# Maximum subarray sum from the array having positive and -ve numbers
# arr = [-1, 3, 4, -2]
# o/p = 7 which is a sum of subarray = 3 + 4
# Naive Approach - O(n^2)

# arr = [-1, 3, 4, -2]
# maxSum = 0
# n = len(arr)
# for i in range(0, n):
#     sum = 0
#     for j in range(i, n):
#         sum += arr[j]
#         maxSum = max(sum, maxSum)
# print(maxSum)

# Kanade's Algorithm - O(n)
# keep adding the elements of the array and keep updating the max sum value,
# if sum becomes less than 0, start from the next index

arr = [-1, -3, -4, -2, 0, 1, 89]
maxSum = arr[0]
sum = arr[0]
for i in arr:
    if sum >= 0:
        sum = sum + i
    else:
        sum = i
    maxSum = max(maxSum, sum)
print(maxSum)
