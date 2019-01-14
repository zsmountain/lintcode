'''
Merge K sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.

Have you met this question in a real interview?  
Example
Given

[
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]
Return

[(1,3),(4,8),(9,10)]
'''


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

import heapq

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        data, res = [], []
        for interval in intervals:
            for i in interval:
                heapq.heappush(data, (i.start, i.end))
        while data:
            interval = heapq.heappop(data)
            self.append(res, interval)
        return res

    def append(self, intervals, interval):
        interval = Interval(interval[0], interval[1])
        if not intervals:
            intervals.append(interval)
            return
        last = intervals[-1]
        if last.end < interval.start:
            intervals.append(interval)
            return
        last.end = max(last.end, interval.end)


s = Solution()
res = s.mergeKSortedIntervalLists([[Interval(1, 3), Interval(4, 7), Interval(6, 8)], [
                         Interval(1, 2), Interval(9, 10)]])
print([(interval.start, interval.end) for interval in res])
