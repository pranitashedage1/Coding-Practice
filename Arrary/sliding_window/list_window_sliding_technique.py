# given an array and int k. Find the max sum of K consecutive elements
# [1, 8, 30, -5, 20, 7]  and k = 3 
# 1 + 8 + 30 = 39
# 3 + 30 + -5 = 28
# 30 + -5 + 20 = 45
# -5 + 20 + 7 = 22

# maximum of > 39, 28, 45, 22 
#  therefore output should be 45

l1 = [1, 8, 30, -5, 20, 7]
k = 3
sum = 0
for i in range(k):
    sum += l1[i]

max_sum = sum
for i in range(k, len(l1)):
    sum += (l1[i]-l1[i-k])
    max_sum = max(sum, max_sum)

print(max_sum)