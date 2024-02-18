'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        intervals.sort(key = lambda i: i[0])
        output.append(intervals[0])

        for start, end in intervals[1:]:
            lastIntervalEnd = output[-1][1]
            if lastIntervalEnd < start:
                output.append([start, end])
            else:
                # [1, 5], [2, 4] > max index from 5 and 4  is 5 So, > [1, 5]
                output[-1][1] = max(end, lastIntervalEnd)
        return output
