'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Have you met this question in a real interview?  
Example
Given s = "bbbab" return 4
One possible longest palindromic subsequence is "bbbb".
'''

class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i+1][j-1] + 2, dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s) - 1]

s = Solution()
print(s.longestPalindromeSubseq('bbbab'))