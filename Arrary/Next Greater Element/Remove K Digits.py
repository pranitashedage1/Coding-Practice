'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''
from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num)
        
        # corner case
        if k == length:
            return "0"
        
        stack = deque()
        i = 0
        
        while i < len(num):
            # whenever meet a digit which is less 
            # than the previous digit, discard 
            # the previous one
            while k > 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        
        # corner case like "1111" or “12345” k=3
        while k > 0:
            stack.pop()
            k -= 1
        
        # construct the number from the stack
        result = "".join(stack[::-1])
        
        # remove all the 0 at the head
        while len(result) > 1 and result[0] == '0':
            result = result[1:]
        
        return result
