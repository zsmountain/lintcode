'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

m and n will be at most 100.

Have you met this question in a real interview?  
Example
Example 1:
	Input: [[0]]
	Output: 1


Example 2:
	Input:  [[0,0,0],[0,1,0],[0,0,0]]
	Output: 2
	
	Explanation:
	Only 2 different path.
'''

class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                elif i == 0:
                    dp[i][j] = dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
                elif j == 0:
                    dp[i][j] = dp[i-1][j] if obstacleGrid[i][j] == 0 else 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
        return dp[m-1][n-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0, 0], [0, 0], [0, 0], [1, 0], [0, 0]]))
print(s.uniquePathsWithObstacles([[0]]))
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
