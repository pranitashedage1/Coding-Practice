'''
You are given a list of songs where the ith song has a duration of time[i] seconds.
Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
'''
from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_count = {}
        count = 0
        for t in time:
           # Calculate the complement remainder that would make the sum divisible by 60
            complement = (60 - (t%60)) % 60
           # Add the number of times the complement has been seen to the count
            count += remainder_count.get(complement, 0)
           # Record the current song's remainder, incrementing the count if it's already been seen
            remainder_count[t%60] = remainder_count.get((t%60), 0) + 1

        return count

print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))
