
'''
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

The subarray should contain at least one number

Have you met this question in a real interview?  
Example
Example 1:

Input:
[1, 3, -1, 2, -1, 2]
Output:
7
Explanation:
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
Example 2:

Input:
[5,4]
Output:
9
Explanation:
the two subarrays are [5] and [4].
'''

import math

class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        # write your code here
        prefix_sum, min_sum, max_sum = 0, 0, -math.inf
        left = [0 for _ in range(len(nums))]
        right = [0 for _ in range(len(nums))]
        res = -math.inf

        for i, num in enumerate(nums):
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            left[i] = max_sum

        prefix_sum, min_sum, max_sum = 0, 0, -math.inf
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            right[i] = max_sum

        for i in range(len(nums) - 1):
            res = max(res, left[i] + right[i+1])

        return res

s = Solution()
print(s.maxTwoSubArrays([1, 3, -1, 2, -1, 2]))
print(s.maxTwoSubArrays([5, 4]))
