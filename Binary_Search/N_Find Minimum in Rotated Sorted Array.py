'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]
        # Initializing pointers
        l, r = 0, len(nums)-1
         # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[r] > nums[0]:
            return nums[0]  
        # Binary search way
        while l <= r:    
            m = l + (r - l) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[m] < nums[m - 1]:
                return nums[m]
            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[m] > nums[0]:
                l = m + 1
            else:
                # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
                r = m - 1
