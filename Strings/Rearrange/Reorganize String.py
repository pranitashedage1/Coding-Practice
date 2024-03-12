'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.
Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
'''
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)
        max_count, letter = 0, 0
        for char, count in char_count.items():
            if count > max_count:
                max_count = count
                letter = char

        if max_count > (len(s)+1) // 2:
            return ""
        
        ans = [""] * len(s)
        index = 0

        # place the most frequent char in the string
        while char_count[letter] != 0:
            ans[index] = letter
            index += 2
            char_count[letter] -= 1
        
        # place rest of the lerrers in any order
        for char, count in char_count.items():
            while count>0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1
            
        return ''.join(ans)
