'''
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.

Have you met this question in a real interview?  
Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).

Challenge
Do it in O(nlogn) time complexity.
'''

import math

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        # write your code here
        if not nums:
            return 0
        nums.sort()
        left, right = 0, len(nums) - 1
        min_diff = math.inf
        while left < right:
            if nums[left] + nums[right] < target:
                min_diff = min(min_diff, abs(nums[left] + nums[right] - target))
                left += 1
            elif nums[left] + nums[right] > target:
                min_diff = min(min_diff, abs(nums[left] + nums[right] - target))
                right -= 1
            else:
                return 0
        return min_diff

s = Solution()
print(s.twoSumClosest([-1, 2, 1, -4], 4))
