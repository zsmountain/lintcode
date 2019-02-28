'''
Given a collection of intervals, merge all overlapping intervals.

Have you met this question in a real interview?  
Example
Example 1:
	Input: [(1,3)]
	Output: [(1,3)]

Example 2:
	Input:  [(1,3),(2,6),(8,10),(15,18)]
	Output: [(1,6),(8,10),(15,18)]

Challenge
O(n log n) time and O(1) extra space.
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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        res = []
        for interval in intervals:
            if not res or interval.start > res[-1].end:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)
        return res