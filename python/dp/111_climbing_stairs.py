'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Have you met this question in a real interview?  
Example
Example 1:
	Input:  n = 3
	Output: 3
	
	Explanation:
	1) 1, 1, 1
	2) 1, 2
	3) 2, 1
	total 3.


Example 2:
	Input:  n = 1
	Output: 1
	
	Explanation:  
	only 1 way.
'''

class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n < 2:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]

s = Solution()
print(s.climbStairs(3))