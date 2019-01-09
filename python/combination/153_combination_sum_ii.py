'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.

Example
Given candidate set [10,1,6,7,2,1,5] and target 8,

A solution set is:

[
  [1,7],
  [1,2,5],
  [2,6],
  [1,1,6]
]
'''

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        # write your code here
        num.sort()
        res = []
        self.helper(num, target, res, [])
        return res

    def helper(self, num, target, res, cur):
        if sum(cur) == target:
            res.append(cur[:])
            return 
        for i in range(len(num)):
            if sum(cur) + num[i] <= target and not (i > 0 and num[i] == num[i-1]):
                cur.append(num[i])
                self.helper(num[i+1:], target, res, cur)
                cur.pop()

s = Solution()
print(s.combinationSum2([3, 1, 3, 5, 1, 1], 8))
print(s.combinationSum2([10, 1, 6, 7, 2, 1, 5], 8))
