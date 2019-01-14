'''
Merge two sorted (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

The intervals in the given list do not overlap.
The intervals in different lists may overlap.
Have you met this question in a real interview?  
Example
Given list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)], return [(1,4),(5,6)].
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

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        # write your code here
        res = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.append(res, list1[i])
                i += 1
            else:
                self.append(res, list2[j])
                j += 1
        while i < len(list1):
            self.append(res, list1[i])
            i += 1
        while j < len(list2):
            self.append(res, list2[j])
            j += 1
        return res

    def append(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
            return
        last_interval = intervals[-1]
        if interval.start > last_interval.end:
            intervals.append(interval)
            return
        last_interval.end = max(interval.end, last_interval.end)
        
s = Solution()
res = s.mergeTwoInterval([Interval(1, 2), Interval(3, 4)], [Interval(2, 3), Interval(5, 6)])
print([(interval.start, interval.end) for interval in res])