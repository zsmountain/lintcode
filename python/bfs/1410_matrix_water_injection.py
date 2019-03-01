'''
Given a two-dimensional matrix, the value of each grid represents the height of the terrain. The flow of water will only flow up, down, right and left, and it must flow from the high ground to the low ground. As the matrix is surrounded by water, it is now filled with water from (R,C) and asked if water can flow out of the matrix.

The input matrix size is n x n, n <= 200.
Ensure that each height is a positive integer.
Have you met this question in a real interview?  
Example
Example1

Input: 
mat =
[
    [10,18,13],
    [9,8,7],
    [1,2,3]
] and R = 1, C = 1
Output: "YES"
Explanation: 
(1,1) →(1,2)→Outflow.
Example2

Input: 
mat = 
[
    [10,18,13],
    [9,7,8],
    [1,11,3]
] and R = 1, C = 1
Output: "NO"
Explanation: 
Since (1,1) cannot flow to any other grid, it cannot flow out.
'''

from collections import deque

class Solution:
    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """

    def waterInjection(self, matrix, R, C):
        # Write your code here
        q = deque([(matrix[R][C], R, C)])
        delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            val, x, y = q.popleft()
            for dx, dy in delta:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < len(matrix) and 0 <= next_y < len(matrix[0]):
                    if matrix[x][y] > matrix[next_x][next_y]:
                        q.append((matrix[next_x][next_y], next_x, next_y))
                else:
                    return 'YES'
        return 'NO'

s = Solution()

matrix = [
    [10, 18, 13],
    [9, 8, 7],
    [1, 2, 3]
]
print(s.waterInjection(matrix, 1, 1))

matrix = [
    [10, 18, 13],
    [9, 7, 8],
    [1, 11, 3]
]
print(s.waterInjection(matrix, 1, 1))
