'''
A non-negative numbers can be regarded as product of its factors.
Write a function that takes an integer n and return all possible combinations of its factors.

Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combination.
Have you met this question in a real interview?  
Example
Given n = 8
return [[2,2,2],[2,4]]
// 8 = 2 x 2 x 2 = 2 x 4.

Given n = 1
return []

Given n = 12
return [[2,6],[2,2,3],[3,4]]
'''

import math
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        # write your code here
        res = []
        self.helper(n, res, [])
        return res

    def helper(self, n, res, cur):
        for i in range(2,int(math.sqrt(n)) + 1):
            if n % i == 0:
                if len(cur) > 0 and i < cur[-1]:
                    continue
                cur.append(i)
                res.append(cur[:] + [n // i])
                self.helper(n // i, res, cur)
                cur.pop()
    
s = Solution()
print(s.getFactors(8))
print(s.getFactors(50))
