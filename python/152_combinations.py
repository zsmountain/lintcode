'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You don't need to care the order of combinations, but you should make sure the numbers in a combination are sorted.

Example
Given n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4]
]
'''

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        # write your code here
        res = []
        self.helper(0, n, k, res, [])
        return res

    def helper(self, start, end, k, res, cur):
        if len(cur) == k:
            res.append(cur[:])
        for i in range(start, end):
            cur.append(i + 1)
            self.helper(i + 1, end, k, res, cur)
            cur.pop()

s = Solution()
print(s.combine(4, 2))