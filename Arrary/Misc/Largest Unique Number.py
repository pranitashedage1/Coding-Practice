'''
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
Example 1:
Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.

Example 2:
Input: nums = [9,9,8,8]
Output: -1
Explanation: There is no number that occurs only once.
'''
from collections import defaultdict
class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = float('-inf')
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        for i in nums:
            if count[i] == 1:
                if i > max_num:
                    max_num = i
                
        return max_num if max_num != float('-inf') else -1
