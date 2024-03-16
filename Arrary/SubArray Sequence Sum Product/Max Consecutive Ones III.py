'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right, num_zero, maxWindow = 0, 0, 0, 0

        while right < len(nums):
            # Encounter zero on the right, increment zero counter
            # Now the window contains 1 extra zero
            if nums[right] == 0:
                num_zero += 1
            
            while num_zero > k:
                # If zero counter goes above k
                # Decrement zero counter when left encounters zero
                # i.e., reduce the number of zeros in the sliding window
                # Now the window contains 1 less zero
                if nums[left] == 0:
                    num_zero -= 1
                left += 1
            
            if num_zero <= k:
                maxWindow = max(maxWindow, right - left + 1)

            right += 1
        
        return maxWindow
