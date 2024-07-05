'''
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other. If it is not possible to rearrange the string, return an empty string "".

Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.

Example 2:
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.

Example 3:
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
'''
import heapq
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k:
            return ""

        char_map = {}
        # Create a frequency map
        for i in range(len(s)):
            char = s[i]
            char_map[char] = char_map.get(char, 0) + 1
        
        # Create a max heap based on the frequency
        pq = []
        for char, freq in char_map.items():
            heapq.heappush(pq, (-freq, char))
        
        sb = []
        wait_queue = []
        while pq:
            freq, char = heapq.heappop(pq)
            sb.append(char)
            wait_queue.append((freq+1, char)) # Decrease frequency (it was negative)
            
            if len(wait_queue) < k:
                continue
            # Release the character from the wait queue if its time has come
            if wait_queue:
                pop_freq, pop_char = wait_queue.pop(0)
                if pop_freq < 0:# Only add back if there's still frequency left
                    heapq.heappush(pq, (pop_freq, pop_char))

        if len(sb) < len(s):
            return ""
        
        return "".join(sb)
