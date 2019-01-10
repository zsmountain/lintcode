'''
Given a list of numbers with duplicate number in it. Find all unique permutations.

Have you met this question in a real interview?  
Example
For numbers [1,2,2] the unique permutations are:

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
Challenge
Using recursion to do it is acceptable. If you can do it without recursion, that would be great!
'''

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        res = []
        nums = sorted(nums)
        self.helper(nums, res, [])
        return res
        
    def helper(self, nums, res, cur):
        if not nums:
            res.append(cur[:])
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            cur.append(nums[i])
            self.helper(nums[:i] + nums[i+1:], res, cur)
            cur.pop()

s = Solution()
print(s.permuteUnique([1, 2, 2]))
