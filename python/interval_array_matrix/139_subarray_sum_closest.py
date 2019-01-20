'''
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

Have you met this question in a real interview?  
Example
Given [-3, 2, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].

Challenge
O(nlogn) time
'''

import math

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        prefix_sum = [(0, -1)]
        for i, num in enumerate(nums):
            prefix_sum.append((prefix_sum[-1][0] + num, i))
        prefix_sum.sort()
        min_val, res = math.inf, [-1, -1]
        for i in range(1, len(prefix_sum)):
            if prefix_sum[i][0] - prefix_sum[i - 1][0] < min_val:
                min_val = prefix_sum[i][0] - prefix_sum[i - 1][0]
                res = [min(prefix_sum[i][1], prefix_sum[i - 1][1]) + 1, max(prefix_sum[i][1], prefix_sum[i - 1][1])]
        return res

s = Solution()
print(s.subarraySumClosest([-3, 1, 1, -3, 5]))


        
