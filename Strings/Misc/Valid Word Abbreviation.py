'''
A string can be abbreviated by replacing any number of non-adjacent, 
non-empty substrings with their lengths. The lengths should not have leading zeros.
For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

Example 2:
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
'''
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(word) and ptr2 < len(abbr):
            if word[ptr1] == abbr[ptr2]:
                ptr1 += 1
                ptr2 += 1
                continue

            if abbr[ptr2] <'1' or abbr[ptr2] > '9':
                return False

            start = ptr2
            while ptr2 < len(abbr) and '0' <= abbr[ptr2] <= '9':
                ptr2 += 1

            ptr1 += int(abbr[start:ptr2])

        return ptr1 == len(word) and ptr2 == len(abbr)

