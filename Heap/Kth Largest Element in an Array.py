'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
#         # First approach using heap
#         heapq.heapify(nums) 
#         return heapq.nlargest(k, nums)[-1]

# Second approach
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        k = len(nums) - k
        
        while left <= right:
            ptr = self.partition(nums, left, right)
            if ptr < k:
                left = ptr + 1
            elif ptr > k:
                right = ptr - 1
            else:
                return nums[ptr]
        return 0

    def partition(self, nums, left, right):
        pivot = nums[right]
        p = left
        for i in range(left, right):
            if nums[i] <= pivot:
                if p != i:
                    nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[right], nums[p] = nums[p], nums[right]
        return p
    
print(Solution().findKthLargest([3,2,1,5,6,0,4], 2))
