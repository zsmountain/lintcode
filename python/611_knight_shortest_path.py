'''
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if knight can not reached.

source and destination must be empty.
Knight can not enter the barrier.

Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1
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

from collections import deque

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1
        visited = {(i, j): False for i in range(len(grid)) for j in range(len(grid[0]))}
        queue = deque([(source.x, source.y)])
        count = 0
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                if x == destination.x and y == destination.y:
                    return count
                for i, j in [(1,2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                    next_x = x + i
                    next_y = y + j
                    if self.is_valid(grid, next_x, next_y, visited):
                        queue.append((next_x, next_y))
                        visited[(next_x, next_y)] = True
            count += 1
        return -1


    def is_valid(self, grid, x, y, visited):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1 and not visited[(x, y)]

s = Solution()
print(s.shortestPath([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]], Point(2, 0), Point(2, 2)))
print(s.shortestPath([[0, 1, 0],
                      [0, 0, 0],
                      [0, 0, 0]], Point(2, 0), Point(2, 2)))
print(s.shortestPath([[0, 1, 0],
                      [0, 0, 0],
                      [0, 0, 1]], Point(2, 0), Point(2, 2)))
