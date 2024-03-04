'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
# # Time Complexity - O(n*2^n)
from typing import List
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         subset = []
#         def dfs(i):
#             if i >= len(nums):
#                 res.append(subset.copy())
#                 return

#             # Decision to include nums[i]
#             subset.append(nums[i])
#             dfs(i + 1)

#             # Decision not to include nums[i]
#             subset.pop()
#             dfs(i+1)

#         dfs(0)
#         return res
# print(Solution().subsets([1, 2, 3]))

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(list, temp, start):
            list.append(temp.copy())
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(list, temp, i + 1)
                temp.pop()
        
        result = []
        backtrack(result, [], 0)
        return result

# Example usage
sol = Solution()
nums = [1, 2, 3]
print(sol.subsets(nums))
