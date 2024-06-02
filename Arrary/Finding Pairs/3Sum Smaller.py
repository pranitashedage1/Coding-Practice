'''
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0
'''
from typing import List
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            low = i+1
            high = len(nums) - 1
            while low < high:
                total_sum = nums[i] + nums[low] + nums[high]
                if total_sum < target:
                    count += high - low
                    low += 1
                else:
                    high -= 1            
        return count
