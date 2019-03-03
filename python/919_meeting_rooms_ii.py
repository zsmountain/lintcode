'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Have you met this question in a real interview?  
Example
Example 1:

Input：intervals = [(0,30),(5,10),(15,20)]
Output：2
'''
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        meeting_rooms = 0
        ongoing_meetings = 0
        for _, delta in sorted(points):
            ongoing_meetings += delta
            meeting_rooms = max(meeting_rooms, ongoing_meetings)

        return meeting_rooms
