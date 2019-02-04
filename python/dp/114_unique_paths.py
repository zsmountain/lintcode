'''
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

m and n will be at most 100.

Have you met this question in a real interview?  
Example
Example 1:
	Input: n = 1, m = 3
	Output: 1
	
	Explanation:
	Only one path to target position.

Example 2:
	Input:  n = 3, m = 3
	Output: 6
	
	Explanation:
	D : Down
	R : Right
	1) DDRR
	2) DRDR
	3) DRRD
	4) RRDD
	5) RDRD
	6) RDDR
'''

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if (i == 1 and j == 0) or (i == 0 and j == 1):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

s = Solution()
print(s.uniquePaths(3, 3))
