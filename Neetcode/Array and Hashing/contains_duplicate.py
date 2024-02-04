'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
'''
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s1 = set()
        for i in nums:
            if i in s1:
                return True
            s1.add(i)
        return False

s = Solution()
a = s.containsDuplicate([1, 13, 3, 4, 3])
print(a)