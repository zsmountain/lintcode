'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

Have you met this question in a real interview?  
Example
Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as AB (1 2) or L (12).
Example 2:

Input: "10"
Output: 1
'''

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here
        if not s or s.startswith('0'):
            return 0
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2: i]) <= 26 and s[i - 1] != '0':
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i-2: i]) == 10 or int(s[i - 2: i]) == 20:
                dp.append(dp[i - 2])
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]

s = Solution()
print(s.numDecodings('0'))
print(s.numDecodings('12'))
print(s.numDecodings('10'))


        
