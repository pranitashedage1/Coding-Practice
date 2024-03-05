# given n ranges, find the maximum appearing element in the ranges.
# i/p - L = [1, 2, 3, 15]
#     - R = [5, 8, 7, 18]
# o/p = 5

# in the above question, ranges of (1, 5) > [1, 2, 3, 4, 5]
#                        ranges of (2, 8) > [2, 3, 4, 5, 6, 7, 8]
#                        ranges of (5, 7) > [5, 6, 7]
#                        ranges of (15, 17) > [15, 16, 17]

#  from above, 5 appears in all the ranges so, o/p will be 5
# For this problem, the range of numbers is limited so we can use the below method. \
#  suppose the range is 1000 which will take O(n) time.

# L = [1, 2, 3, 15]
# R = [5, 8, 7, 18]
L = [1, 2, 3]
R = [3, 5, 7]
# L = [1, 0, 4, 2, 5, 6, 3, 4]
# R = [2, 3, 5, 4, 6, 7, 6, 8]
arr = [0] * 50 # here add instead of 50 multiply by 1000 and create a array of 1000 element.
#  Here, for covenience, I created an array of 50
n = len(L)
for i in range(n):
    arr[L[i]] = arr[L[i]] + 1
    arr[R[i]+1] = arr[R[i]+1] - 1
print(arr)
maxm = arr[0]
result = 0
for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i-1]
    if arr[i] >= maxm:
        maxm = arr[i]
        result = i
print(arr)
print(result)
