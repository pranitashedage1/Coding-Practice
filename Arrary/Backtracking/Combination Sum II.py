'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''
from typing import List
class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.combinations(candidates, [], 0, 0, target)
        return self.res

    def combinations(self, nums: List[int], lst: List[int], start: int, total: int, target: int):
        if total == target:
            self.res.append(lst[:])

        if total > target:
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            lst.append(nums[i])
            total += nums[i]
            self.combinations(nums, lst, i + 1, total, target)
            total -= nums[i]
            lst.pop()
