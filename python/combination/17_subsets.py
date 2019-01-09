'''
Given a set of distinct integers, return all possible subsets.

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Challenge
Can you do it in both recursively and iteratively?
'''

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        nums.sort()
        res = []
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, cur):
        res.append(cur[:])
        for i, num in enumerate(nums):
            cur.append(num)
            self.helper(nums[i+1:], res, cur)
            cur.pop()


s = Solution()
print(s.subsets([1, 2, 3]))