'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Have you met this question in a real interview?  
Example
example 1
Given the following triangle:

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

example 2
Given the following triangle:

[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).
'''

import math

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        dp = [ [math.inf for i in range(n)] for n in range(1, len(triangle) + 1) ]
        dp[0][0] = triangle[0][0]
        res = math.inf
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + triangle[i][j])
                elif j == i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]) + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
                if i == len(triangle) - 1:
                    res = min(res, dp[i][j])
        return res

s = Solution()
triangle = [[1], [2, 3]]
print(s.minimumTotal(triangle))
triangle = [[-10]]
print(s.minimumTotal(triangle))
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(s.minimumTotal(triangle))
triangle = [
    [2],
    [3, 2],
    [6, 5, 7],
    [4, 4, 8, 1]
]
print(s.minimumTotal(triangle))
