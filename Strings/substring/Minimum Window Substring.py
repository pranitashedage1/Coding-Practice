'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        start, end = 0, 0
        minLength = float('inf')
        # Create a dictionary for all the chars from string t and their freq.
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        # create a counter to maintain the condition - all the chars from t should be in the substring of s. (including duplicates from t)
        count = len(countT)
        head = 0
        while end < len(s):
            char = s[end]
            if char in countT:
                # Here we will decrease the frequency as we encounter the char in s.
                countT[char] -= 1
                #  when that particular char from s reaches to its highest frequency maching to its frequency from string t that means, countT[char] will be 0. 
                # then we will reduce the count by 1.
                if countT[char] == 0:
                    count -= 1
            end += 1
            #  when count will reach to 0 means all chars from t are found in s. now we need to reduce the string length.
            while count == 0:
                temp = s[start]
                if temp in countT:
                    countT[temp] += 1
                    if countT[temp] > 0:
                        count += 1
            # here we will monitor the minimum lenght
                if end - start < minLength:
                    minLength = end - start
                    head = start
                start += 1
        return '' if minLength == float('inf') else s[head:head + minLength]
