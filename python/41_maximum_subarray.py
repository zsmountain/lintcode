'''
Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Challenge
Can you do it in time complexity O(n)?

'''

import sys

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        prefix_sum, min_sum, max_sum = 0, 0, -sys.maxsize
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
        return max_sum

s = Solution()
print(s.maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
