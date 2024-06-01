'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # By swapping - testcase - [1,0,3,0,12]
        # snowball = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[i - snowball], nums[i] = nums[i], nums[i - snowball]
        #     else:
        #         snowball += 1

        # By swapping - testcase - [1,0,3,0,12] - for this testcase, for the first index, 1 is getting swap with itself only. This can be avoided by below test case.
        # snowball = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0 and snowball != 0:
        #         nums[i - snowball], nums[i] = nums[i], nums[i - snowball]
        #     elif nums[i] == 0:
        #         snowball += 1

        # By left and right pointer approach
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1 

        while left < len(nums):
            nums[left] = 0
            left += 1
