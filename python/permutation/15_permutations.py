'''
Given a list of numbers, return all possible permutations.

You can assume that there is no duplicate numbers in the list.

Have you met this question in a real interview?  
Example
For nums = [1,2,3], the permutations are:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Challenge
Do it without recursion.
'''

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        res = []
        self.helper(nums, res, [])
        return res
    
    def helper(self, nums, res, cur):
        if not nums:
            res.append(cur[:])
            return 
        for i in range(len(nums)):
            cur.append(nums[i])
            self.helper(nums[:i] + nums[i+1:], res, cur)
            cur.pop()

    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        permulations = self.permute(nums[1:])
        res = []
        for permulate in permulations:
            for i in range(len(permulate) + 1):
                new = permulate[:i] + [nums[0]] + permulate[i:]
                res.append(new)
        return res

    def permute(self, nums):
        if not nums:
            return [[]]
        result = []
        stack = [[i] for i in nums]
        while stack:
            last = stack.pop()
            if len(last) == len(nums):
                result.append(last)
                continue
            for n in nums:
                if n not in last:
                    stack.append(last + [n])
        return result
        
s = Solution()
print(s.permute([1, 2, 3]))
