'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, total_sum, final_len = 0, 0, 0, float('inf')
        while end < len(nums):
            total_sum += nums[end]
            end += 1
            while total_sum >= target:
                final_len = min(final_len, end - start)
                total_sum -= nums[start]
                start += 1
        return final_len if final_len != float('inf') else 0
