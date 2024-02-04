'''
Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
# First Approach - 
# Time complexity - O(n)
# Space complexity - O(n)
# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         length = len(nums)
#         L, R , answer = [0] * length, [0] * length, [0] * length

#         L[0] = 1
#         for i in range(1, length):
#             L[i] = L[i-1] * nums[i-1]
        
#         R[length - 1] = 1
#         for i in range(length-2, -1, -1):
#             R[i] = R[i+1] * nums[i+1]
        
#         for i in range(length):
#             answer[i] = L[i] * R[i]

#         return answer


# Second Approach -
# time complexity - O(n)
# space complexity - O(1) - Here we are not considering the answer array sapce. That is why, space is O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1, length):
           answer[i] =  answer[i-1] * nums[i-1]
        
        right = 1
        for i in range(length-1, -1, -1):
            answer[i] = right * answer[i]
            right *= nums[i]
        
        return answer

print(Solution().productExceptSelf([1, 2, 3, 4]))
