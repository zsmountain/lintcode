'''
Given an integer arrays, find a contiguous subarray which has the largest sum and length should be greater or equal to given length k.
Return the largest sum, return 0 if there are fewer than k elements in the array.

Ensure that the result is an integer type.
k > 0
Have you met this question in a real interview?  
Example
Given the array [-2,2,-3,4,-1,2,1,-5,3] and k = 5, the contiguous subarray [2,-3,4,-1,2,1] has the largest sum = 5.
'''

import math

class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """

    def maxSubarray4(self, nums, k):
        # write your code here
        if len(nums) < k:
            return 0
        prefix_sum = [0]
        min_prefix = math.inf
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])
        res = -math.inf
        for i in range(k, len(prefix_sum)):
            min_prefix = min(min_prefix, prefix_sum[i - k])
            res = max(res, prefix_sum[i] - min_prefix)
        return res

s = Solution()
print(s.maxSubarray4([5], 1))
print(s.maxSubarray4([-2, 2, -3, 4, -1, 2, 1, -5, 3], 5))
