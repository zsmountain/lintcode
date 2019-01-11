'''
Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.

Have you met this question in a real interview?  
Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
'''
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

import heapq

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        heap = []
        res = []
        for point in points:
            heapq.heappush(heap, ((point.x - origin.x) * (point.x - origin.x) + (point.y - origin.y) * (point.y - origin.y), point.x, point.y))
        for i in range(k):
            _, x, y = heapq.heappop(heap)
            res.append(Point(x, y))
        return res
        
s = Solution()
points = [Point(4, 6), Point(4, 7), Point(4, 4), Point(2, 5), Point(1, 1)]
res = s.kClosest(points, Point(0, 0), 3)
for point in res:
    print(point.x, point.y)
