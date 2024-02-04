# Fibonacci Series
#0,0,0,1,1,2,4,8,15,29
# below solution is a simple approach - This solution takes O(n * m) time
# n = 4
# m = 10
# l1 = [0]* (n-1) + [1]
# print(l1)
# start = 0
# # []
# for i in range(n, m):
#     sum = 0
#     for j in range(start, start+n):
#         sum = sum + l1[j]
#     l1.append(sum)
#     start = start + 1
# print(l1)

# below solution takes O(m) time
n = 3
m = 10
l1 = [0]* (n-1) + [1, 1]
start = 0
end = n
print(l1)
next_element = 1
for i in range(end, m-1):
    next_element = next_element - l1[i - n]
    next_element = next_element + l1[i]
    l1.append(next_element)
print(l1)

