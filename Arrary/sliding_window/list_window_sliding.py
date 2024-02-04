# given an array and int k. Find the array whose sum of K consecutive elements is equal to 45
# [1, 8, 30, -5, 20, 7]  and k = 3 
# 1 + 8 + 30 = 39
# 3 + 30 + -5 = 28
# 30 + -5 + 20 = 45
# -5 + 20 + 30 = 45

# therefore print the output of those array whose sum is 45

l1 = [1, 8, 30, -5, 20, 30]
k = 3
sum = 0
for i in range(k):
    sum += l1[i]
if sum == 45:
    print(l1[:k])

for i in range(k, len(l1)):
    sum += (l1[i] - l1[i-k])
    if sum == 45:
        print(l1[(i-k+1):i+1])
