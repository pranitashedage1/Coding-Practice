'''
Given an integer array nums of unique elements, return all possible 
subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(result, [], 0, nums)
        return result

    def backtrack(self, result, temp, start, nums):
        result.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(result, temp, i+1, nums)
            temp.pop()     
