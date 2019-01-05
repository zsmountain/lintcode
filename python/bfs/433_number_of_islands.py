'''
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.
'''

from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        res = 0
        if not grid or not grid[0]:
            return res
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    self.bfs(grid, i, j)
                    res += 1

        return res
        
    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = 0
        while queue:
            x, y = queue.popleft()
            delta_x = [1, -1, 0, 0]
            delta_y = [0, 0, 1, -1]
            for k in range(4):
                next_x = x + delta_x[k]
                next_y = y + delta_y[k]
                if self.isValid(grid, next_x, next_y):
                    queue.appendleft((next_x, next_y))
                    grid[next_x][next_y] = 0

    def isValid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1
 

s = Solution()
print(s.numIslands([
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1]
]))
