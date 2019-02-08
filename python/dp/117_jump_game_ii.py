'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Have you met this question in a real interview?  
Example
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

import math

class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        # write your code here
        n = len(A)
        dp = [math.inf for _ in range(n)]
        dp[0] = 0
        for i in range(n):
            if dp[i] == math.inf:
                continue
            for j in range(A[i]):
                if i + j + 1 >= n:
                    break
                dp[i+j+1] = min(dp[i+j+1], dp[i] + 1)
        return dp[-1]

s = Solution()
print(s.jump([2, 3, 1, 1, 4]))