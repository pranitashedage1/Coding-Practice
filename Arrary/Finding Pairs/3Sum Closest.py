'''
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        res = float('inf')
        for i in range(len(nums)-2):
            low = i + 1
            high = len(nums)-1
            while low < high:
                total_sum = nums[i] + nums[low] + nums[high]
                diff = abs(target - total_sum)
                if diff < min_diff:
                    min_diff = diff
                    res = total_sum
                if total_sum < target:
                    low += 1
                elif total_sum > target:
                    high -= 1
                else:
                    return total_sum
        return res
