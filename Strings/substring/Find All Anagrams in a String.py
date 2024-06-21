'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
from collections import defaultdict
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        char_map = defaultdict(int)
        for c in p:
            char_map[c] += 1
        count = len(char_map)
        start, end = 0, 0
        while end < len(s):
            c = s[end] 
            if c in char_map:
                char_map[c] -= 1
                if char_map[c] == 0:
                    count -= 1   
            end += 1         
            while count == 0:
                temp = s[start]    
                if temp in char_map:
                    char_map[temp] += 1
                    if char_map[temp] > 0:
                        count += 1
                # we need to make sure substring is anagram of p, that means lenght of substring should be equal to lenght of p.
                if (end - start) == len(p):
                    result.append(start)    
                start += 1  
        return result
