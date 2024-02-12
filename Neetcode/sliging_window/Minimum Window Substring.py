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
        if t == '' : return ''
        countT, window = {}, {}
        # Create a dictionary with value of freq of each char in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        l, r = 0, 0
        have, need = 0, len(countT)
        res, resultLength = [-1, -1], float('infinity')
        l = 0
        # Create a dictionary with value of freq of each char in t
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in t and window[s[r]] == countT[s[r]]:
                have += 1
        #    Remove letter from the left until winodw becomes unsatisfied
            while have == need:
                # when in the window we have our results then we will update our results
                # with the legth of the window
                if (r - l + 1) < resultLength:
                    res = [l, r]
                    resultLength = r - l + 1
                # Once results are update, pop from the left
                window[s[l]] -= 1
                # if left char is from the countT, then resuce the have count
                if s[l] in t and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resultLength != float('infinity') else ''

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
