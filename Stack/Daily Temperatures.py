'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # We will create a stack which will have index and temperature
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                # If stack and current temp is greater than last one then pop the last element
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = (i-stackIndex)
            stack.append([i, t])
        return res

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
