'''
Given an integer array nums that may contain duplicates, return all possible 
subsets(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.backtrack(result, [], 0, nums)
        return result

    def backtrack(self, result, temp, start, nums):
        result.append(temp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.backtrack(result, temp, i + 1, nums)
            temp.pop()
