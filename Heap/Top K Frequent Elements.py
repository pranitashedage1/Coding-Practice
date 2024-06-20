'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''
import heapq
from collections import Counter

class Solution(object):
    def __init__(self):
            self.freq = {}

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        self.freq = Counter(nums)
        unique = list(self.freq.keys())
        return self.quickSelct(unique, k)
        

    def quickSelct(self, unique, k):
        left = 0
        right = len(unique) - 1
        k = len(unique) - k

        while left <= right:
            ptr = self.partition(unique, left, right)
            if ptr < k:
                left = ptr + 1
            elif ptr > k:
                right = ptr - 1
            else:
                break
        return unique[k:]

    def partition(self, unique, left, right):
        pivotFreq = self.getFreq(unique[right])
        p = left
        for i in range(left, right):
            if self.getFreq(unique[i]) <= pivotFreq:
                if p != i:
                    unique[p], unique[i] = unique[i], unique[p]
                p += 1
        unique[p], unique[right] = unique[right], unique[p]
        return p

    def getFreq(self, num):
        return self.freq[num]


class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums

        count = Counter(nums)

        res = []
        for num, freq in count.items():
            heapq.heappush(res, (freq, num))
            if len(res) > k:
                heapq.heappop(res)
    
        output = []
        for num in res:
            output.append(num[1])
        return output
