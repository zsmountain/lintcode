'''
Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.

It's guaranteed that the size of the array is greater or equal to k.

Have you met this question in a real interview?  
Example
Given nums = [1, 12, -5, -6, 50, 3], k = 3

Return 15.667 // (-6 + 50 + 3) / 3 = 15.667
'''

import math

class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        # write your code here
        start, end = min(nums), max(nums)
        while start + 1e-5 < end:
            mid = (start + end) / 2
            if self.has_larger_average(nums, k, mid):
                start = mid
            else:
                end = mid
        return start

    def has_larger_average(self, nums, k, avg):
        prefix_sum = [0]
        min_sum = math.inf
        for i, num in enumerate(nums):
            prefix_sum.append(prefix_sum[-1] - avg + num)
            if i + 1 - k < 0:
                continue
            min_sum = min(min_sum, prefix_sum[i + 1 - k])
            if prefix_sum[-1] >= min_sum:
                return True
        return False

                  
s = Solution()
nums = [1, 12, -5, -6, 50, 3]
print(s.maxAverage(nums, 3))
