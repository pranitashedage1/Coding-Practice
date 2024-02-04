class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        string1 = ''
        p1 , p2 = 0, 0
        while (p1 < n1 or p2 < n2):
            if p1< n1:
                string1 = string1 + word1[p1]
                p1 += 1
            if p2 < n2:
                string1 += word2[p2]
                p2 += 1   
        return string1
