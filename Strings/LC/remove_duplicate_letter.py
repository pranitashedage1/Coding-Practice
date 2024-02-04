# Example 1:
# Input: s = "abbaca"
# Output: "ca"

# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
# and this is the only possible move.  The result of this move is that the string is "aaca", 
# of which only "aa" is possible, so the final string is "ca".

# Example 2:
# Input: s = "azxxzy"
# Output: "ay"

# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         str1 = ''
#         for i in s:
#             if str1:
#                 last = str1[-1]
#                 if last == i:
#                     str1 = str1.replace(str1[-1], '')
#                 else:
#                     str1 += i
#             else:
#                 str1 += i
#         return str1


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
# a = s.removeDuplicates('aabccbdc')
# print(a)
