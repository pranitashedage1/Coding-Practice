'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
'''
# Check next meeting's starting time is only after current meeting time. Then person can attand both
# the meeting.
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key = lambda i : i[0])
        for i in range(len(intervals)-1):
            if intervals[i+1][0] < intervals[i][1]:
                return False
        return True
