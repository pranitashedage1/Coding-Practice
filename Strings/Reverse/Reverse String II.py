'''
Given a string s and an integer k, reverse the first k characters for every 2k characters 
counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but 
greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
'''
class Solution:
    def reverseStr(self, s, k):
        chars = list(s)
        n = len(chars)
        
        def swap(chars, start, end):
            while start < end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1
        
        start = 0
        while start < n:
            end = min(start + k - 1, n - 1)
            swap(chars, start, end)
            start += 2 * k
        
        return ''.join(chars)
