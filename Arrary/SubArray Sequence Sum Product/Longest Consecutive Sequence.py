'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
# Fisrt Approach - Brute Force
# Time complexity - O(n^2)
# Space complextiy - O(1)

# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         longest_streak = 0

#         for num in nums:
#             current_num = num
#             current_streak = 1
            
#             while current_num + 1 in nums:
#                 current_num += 1
#                 current_streak += 1
            
#             longest_streak = max(longest_streak, current_streak)

#         return longest_streak

# print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

# Second Approach - sorting - 
# Time complexity - O(nlogn)
# Space complexity - O(1)

# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         nums.sort()
#         longest_streak = 1
#         current_streak = 1

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 if  nums[i] == nums[i-1] + 1:
#                     current_streak += 1
#                 else:
#                     longest_streak = max(longest_streak, current_streak)
#                     current_streak = 1 
    
#         return max(longest_streak, current_streak)

# Third Approach - Hashset and Intelligent Sequence Building
# Time complexity - O(n) - Although the time complexity appears to be quadratic due to the while
# loop nested within the for loop, closer inspection reveals it to be
# linear. Because the while loop is reached only when currentNum marks
# the beginning of a sequence (i.e. currentNum-1 is not present in
# nums), the while loop can only run for nnn iterations throughout the
# entire runtime of the algorithm. This means that despite looking like
# O(n⋅n)O(n \cdot n)O(n⋅n) complexity, the nested loops actually run in O(n+n)=O(n)O(n + n) = O(n)O(n+n)=O(n)
# time. All other computations occur in constant time, so the overall
# runtime is linear.
# Space complexity - O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_streak = 1
                while current_num + 1 in nums:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
