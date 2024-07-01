'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort()
        first = strs[0]
        last = strs[-1]
        size = min(len(first), len(last))

        for i in range(0, size):
            if first[i] != last[i]:
                return first[:i]
        
        return first[:size]

class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_str, max_str = self.findMinMax(strs)

        size = min(len(min_str), len(max_str))
        for i in range(size):
            if min_str[i] != max_str[i]:
                return min_str[:i]
        
        return min_str[:size]

    def findMinMax(self, strs):
        min_str = strs[0]
        max_str = strs[0]

        for str_i in strs:
            if str_i < min_str:
                min_str = str_i
            if str_i > max_str:
                max_str = str_i

        return min_str, max_str 
