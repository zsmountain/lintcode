'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.

Have you met this question in a real interview?  
Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here
        n = len(A)
        dp = [False for _ in range(n)]
        dp[0] = True
        for i in range(n):
            if dp[i] == False:
                continue
            for j in range(A[i]):
                if i + j + 1 >= n:
                    break
                dp[i+j+1] = True
        return dp[-1]

s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))