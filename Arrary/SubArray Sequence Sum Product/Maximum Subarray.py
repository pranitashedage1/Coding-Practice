'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initilaize our variables using the first element.
        maxSum, currSum = nums[0], nums[0]
        # Start with the second element since we already used the first one
        for num in nums[1:]:
            #  If currentSum is negative, throw is away. Otherwsie keep adding to it.
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        return maxSum
