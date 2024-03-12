'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def backtrack(openN, closedN):
            if closedN == openN == n:
                res.append(''.join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closedN)
                stack.pop()
            # Closed bracket will add only if the number of closed bracket is less
            # than the number of closed bracked is less than the number of open bracket.
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0, 0)
        return res

print(Solution().generateParenthesis(3))
