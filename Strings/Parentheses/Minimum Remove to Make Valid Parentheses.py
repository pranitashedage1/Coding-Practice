'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Pass 1: Remove all invalid ")"
        sb = []
        open_seen = 0
        balance = 0
        
        for c in s:
            if c == '(':
                open_seen += 1
                balance += 1
            if c == ')':
                if balance == 0:
                    continue
                balance -= 1
            sb.append(c)
        
        # Pass 2: Remove the rightmost "("
        result = []
        open_to_keep = open_seen - balance
        
        for c in sb:
            if c == '(':
                if open_to_keep <= 0:
                    continue
                open_to_keep -= 1
            result.append(c)
        
        return ''.join(result)

