'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        stack = []
        if n%2 != 0:
            return False
        else:
            map_signs = {')':'(', '}':'{', ']':'['}
            for char in s:
                if char in map_signs:
                    top_element = stack.pop() if stack else '#'

                    if map_signs[char] != top_element:
                        return False
                else:
                    stack.append(char)
        
        return not stack
