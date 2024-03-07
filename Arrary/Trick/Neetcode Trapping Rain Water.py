# l1 = [3,0,5,0,3,0,1,0,6]
# l1 = [3, 2, 1, 6, 2, 0, 1, 0, 8]
# l1 = [3,2,1,0]
# sum = 0
# for i in range(1, len(l1)-1):
#     a = max(l1[:i+1])
#     b = max(l1[i:])
#     if a == l1[i] or b == l1[i]:
#         c = 0
#     else:
#         c = min(a, b) - l1[i]
#     sum = sum + c
# print(sum)

# left_max, right_max = [0] * len(l1), [0] * len(l1)

# left_max[0] = l1[0]
# print(left_max)
# for i in range(1, len(l1)):
#     left_max[i] = max(left_max[i-1], l1[i])
#     print("left_max = ", left_max)

# right_max[len(l1)-1] = l1[len(l1)-1]
# print(right_max)
# for i in range(len(l1)-2, -1, -1):
#     right_max[i] = max(right_max[i+1], l1[i])
#     print("left_max = ", right_max)

# water = 0
# for i in range(0, len(l1)):
#     water = water +  min(left_max[i], right_max[i]) - l1[i]
# print(water)


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res
