'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
# ![container with most water](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
'''
# Container with most water
# Time Complexity - O(n)
# Space Complexity - O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low, high = 0, len(height)-1
        max_water = 0
        while low < high:
            current_water = min(height[low], height[high]) * (high - low)
            max_water = max(current_water, max_water)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1      
        return max_water

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
