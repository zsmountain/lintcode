'''
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

Have you met this question in a real interview?  
Example
Given a matrix:

0 1 2 0 0
1 0 0 2 1
0 1 0 0 0
return 2
'''

from collections import deque

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1

        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j))
                    
        level = 0
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            level += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in delta:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 0:
                        grid[x + dx][y + dy] = 1
                        q.append((x+dx, y + dy))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return -1

        return level - 1

s = Solution()
grid = [
    [0, 1, 2, 0, 0],
    [1, 0, 0, 2, 1],
    [0, 1, 0, 0, 0]
]
print(s.zombie(grid))
