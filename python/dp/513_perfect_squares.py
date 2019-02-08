'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Have you met this question in a real interview?  
Example
Given n = 12, return 3 because 12 = 4 + 4 + 4
Given n = 13, return 2 because 13 = 4 + 9
'''

class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # write your code here
        dp = [n for _ in range(n+1)]
        for i in range(n+1):
            if i**2 <= n:
                dp[i**2] = 1
            j = 1
            while j**2 < i:
                dp[i] = min(dp[i], dp[i-j**2] + 1)
                j += 1
        return dp[n]

s = Solution()
print(s.numSquares(12))
print(s.numSquares(13))