'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any 
position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing 
parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:
Input: s = "())"
Output: 1

Example 2:
Input: s = "((("
Output: 3
'''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # To track if open parenthesis is not balanced
        open_case = 0
        # To track if close parenthesis is not balanced
        close_case = 0

        for c in s:
            if c == '(':
                open_case += 1
            elif c == ')':
                # For test cases where open parenthesis is balanced but close parenthesis is not
                # e.g., ()))()((
                if open_case == 0:
                    close_case += 1
                else:
                    open_case -= 1

        return open_case + close_case
