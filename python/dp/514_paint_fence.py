'''
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

n and k are non-negative integers.

Have you met this question in a real interview?  
Example
Example 1:

Input: n=3, k=2  
Output: 6
Explanation:
          post 1,   post 2, post 3
    way1    0         0       1 
    way2    0         1       0
    way3    0         1       1
    way4    1         0       0
    way5    1         0       1
    way6    1         1       0
Example 2:

Input: n=2, k=2  
Output: 4
Explanation:
          post 1,   post 2
    way1    0         0       
    way2    0         1            
    way3    1         0          
    way4    1         1       
'''

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def numWays(self, n, k):
        # write your code here
        if n < 1:
            return 0
        if n == 1:
            return k
        dp = [0 for _ in range(n+1)]
        dp[1] = k
        dp[2] = k * k
        for i in range(3, n + 1):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])
        return dp[n]

s = Solution()
print(s.numWays(7, 6))
print(s.numWays(1, 1))
print(s.numWays(3, 2))
print(s.numWays(2, 2))