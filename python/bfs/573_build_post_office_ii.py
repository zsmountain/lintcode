'''
Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.
Have you met this question in a real interview?  
Example
Given a grid:

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
return 8, You can build at (1,1). (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)

Challenge
Solve this problem within O(n^3) time.
'''

from collections import deque
import math

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1

        min_dist = math.inf
        dist_map = {}
        house_count_map = {}
        total_house = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_house += 1
                    self.bfs(i, j, grid, dist_map, house_count_map)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i, j) in house_count_map and house_count_map[(i, j)] == total_house:
                    min_dist = min(min_dist, dist_map[(i, j)])

        return min_dist if min_dist != math.inf else -1

    def bfs(self, x, y, grid, dist_map, house_count_map):
        visited = set()
        q = deque([(x, y)])
        visited.add((x, y))
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in delta:
                    next_x = x + dx
                    next_y = y + dy
                    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == 0 and (next_x, next_y) not in visited:
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))
                        if (next_x, next_y) in dist_map:
                            dist_map[(next_x, next_y)] += step
                            house_count_map[(next_x, next_y)] += 1
                        else:
                            dist_map[(next_x, next_y)] = step
                            house_count_map[(next_x, next_y)] = 1
            step += 1

s = Solution()
grid = [
    [0, 1, 0, 0, 0],
    [1, 0, 0, 2, 1],
    [0, 1, 0, 0, 0]]
print(s.shortestDistance(grid))
