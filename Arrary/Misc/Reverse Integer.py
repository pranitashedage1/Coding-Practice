'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the 
value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 
Constraints:
-231 <= x <= 231 - 1
'''
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        num = 0
        x = abs(x)
        while x:  
            mod = x % 10
            x = int(x/10)
            num = num * 10 + mod
            if num > 2**31 - 1:
                return 0
        return num * sign
