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
        # First approach using heap
        # # Total time complexity - O(n + k log n)
        # heapq.heapify(nums) # time complexity - O(n)
        # return heapq.nlargest(k, nums)[-1] # Time complexity - O(k log n)

        # Second apprach using quick select
        # Time complexity - Average case - O(n^2)
        # Time complexity - Worst Case - O(n^2)
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > k:
                # number will be on the right side
                return quickSelect(l, p-1)
            elif p < k:
                # number is on the left side
                return quickSelect(p+1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums)-1)

print(Solution().findKthLargest([3,2,1,5,6,0,4], 2))
