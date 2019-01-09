'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

Example
Input: [1,2,2]
Output:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        res = []
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, cur):
        res.append(cur[:])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cur.append(nums[i])
            self.helper(nums[i+1:], res, cur)
            cur.pop()

s = Solution()
print(s.subsetsWithDup([1, 2, 2]))