'''
Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?

Have you met this question in a real interview?  
Example
Given n = 3, there are a total of 5 unique BST's.

1           3    3       2      1
 \         /    /       / \      \
  3      2     1       1   3      2
 /      /       \                  \
2     1          2                  3
'''
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        dp = [1, 1]
        if n <= 1:
            return dp[n]
        dp += [0 for _ in range(n-1)]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]

s = Solution()
print(s.numTrees(3))