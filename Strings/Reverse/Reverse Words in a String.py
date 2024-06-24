'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces 
between two words. The returned string should only have a single space separating the words. 
Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
class Solution:
    def reverseWords(self, s):
        def reverse(str_list, start, end):
            while start < end:
                str_list[start], str_list[end] = str_list[end], str_list[start]
                start += 1
                end -= 1

        str_list = list(s)
        n = len(str_list)
        
        # Reverse the entire string
        reverse(str_list, 0, n - 1)
        
        store_index = 0
        l = 0
        
        while l < n:
            if str_list[l] != ' ':
                if store_index != 0:
                    str_list[store_index] = ' '
                    store_index += 1
                
                r = l
                while r < n and str_list[r] != ' ':
                    if store_index < n:
                        str_list[store_index] = str_list[r]
                    store_index += 1
                    r += 1
                
                # Reverse the current word in place
                reverse(str_list, store_index - (r - l), store_index - 1)
                l = r
            l += 1
        
        return ''.join(str_list[:store_index])
