# Given an array of integers, find if it has an equilibrium point.
# if the sum of the left side and right of the element is equal then that element is an equilibrium.
# l1 = [3,4,8,-9,20,6] - In this 20 is an equilibrium.
# l1 = [4, 2, -2] - In this 4 is an equilibrium, there is no element on the left side of 4
# so the left side sum of 4 is 0 and the right side sum is also 0.

# l1 = [4, 2, -2]
# l1 = [2, 6, 0]
# l1 = [3,4,8,-9,20,6]
# def equi(l1, n):
#     for i in range(0, n):
#         left_sum, right_sum = 0, 0
#         for j in range (0, i):
#             left_sum = left_sum + l1[j]
#         for k in range(i+1, n):
#             right_sum = right_sum + l1[k]
#         if right_sum == left_sum:
#             return True
#     return False

# a = equi(l1, len(l1))
# print(a)

l1 = [4, 2, -2]
# l1 = [2, 6, 0]
# l1 = [3,4,8,-9,20,6]
def equi(l1, n):
    total_sum = 0
    for i in range(n):
        total_sum += l1[i]
    left_sum = 0
    for i in range(n):
        if (left_sum == (total_sum - l1[i])):
            return True
        left_sum += l1[i]
        total_sum -= l1[i]
    return False
a = equi(l1, len(l1))
print(a)
