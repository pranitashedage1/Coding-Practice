'''
Given a string num which represents an integer, return true if num is a strobogrammatic number.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false
'''
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        rotated_digits = {'0':'0', '1':'1', '6':'9', '9':'6', '8':'8'}
        left = 0
        right = len(num)-1
        while left <= right:
            if num[left] not in rotated_digits or rotated_digits[num[left]] != num[right]:
                return False
            left += 1
            right -= 1

        return True
