'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            low = i+1
            high = len(nums) - 1
            while low < high:
                total_sum = num + nums[low] + nums[high]
                if total_sum < 0:
                    low += 1
                elif total_sum > 0:
                    high -= 1
                else:
                    res.append([num, nums[low], nums[high]])
                    low += 1
                    while nums[low] == nums[low-1] and low < high:
                        low += 1
        return res
print(Solution().threeSum([-3, 3, 3, 4, -3, 1, 2, 0, 1, 2]))

# TODO: Check other approach afterwards - 
