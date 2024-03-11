'''
You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []
        for i in s:
            if output and output[-1] == i:
                output.pop()
            else:
                output.append(i)
        return ''.join(output)

s = Solution()
a = s.removeDuplicates('aababaab')
print(a)

# from string import ascii_lowercase
# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         # generate 26 possible duplicates
#         duplicates = {2 * ch for ch in ascii_lowercase}    
#         prev_length = -1
#         while prev_length != len(S):
#             prev_length = len(S)
#             for d in duplicates:
#                 S = S.replace(d, '')               
#         return S

# s = Solution()
# a = s.removeDuplicates('aababaab')
# print(a)
