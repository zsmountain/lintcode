'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.

Example
Given candidate set [2,3,6,7] and target 7, a solution set is:

[7]
[2, 2, 3]
'''

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        res = []
        self.helper(candidates, target, res, [])
        return res

    def helper(self, candidates, target, res, cur):
        if sum(cur) == target:
            res.append(cur[:])
            return
        for i in range(len(candidates)):
            if (i > 0 and candidates[i-1] == candidates[i]):
                continue
            if sum(cur) + candidates[i] <= target:
                cur.append(candidates[i])
                if sum(cur) + candidates[i] <= target:
                    self.helper(candidates[i:], target, res, cur)
                else:
                    self.helper(candidates[i+1:], target, res, cur)
                cur.pop()

s = Solution()
print(s.combinationSum([1, 1, 1], 2))
print(s.combinationSum([2, 3, 6, 7], 7))
