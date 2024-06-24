'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, 
more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''
class Solution:
    def reverseVowels(self, ss):
        if ss == "":
            return ss
        
        s = list(ss)
        ptr1, ptr2 = 0, len(s) - 1
        vowels = set('aeiouAEIOU')
        
        while ptr1 < ptr2:
            if s[ptr1] in vowels and s[ptr2] in vowels:
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1
            while ptr1 < ptr2 and s[ptr1] not in vowels:
                ptr1 += 1
            while ptr2 > ptr1 and s[ptr2] not in vowels:
                ptr2 -= 1
        return ''.join(s)
