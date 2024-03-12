'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
'''
import heapq
class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(n)
        list1 = [(-nums[i], i) for i in range(len(nums))]
        # O(log n)
        heapq.heapify(list1)
        ans = []
        # O(k log n)
        while k > 0:
            ans.append(heapq.heappop(list1))
            k -= 1    
        # O(n log n)
        ans.sort(key= lambda k: k[1])
        return [-i[0] for i in ans]

print(Solution().maxSubsequence([2,1,3,3], k = 2))
