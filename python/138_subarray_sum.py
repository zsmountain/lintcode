'''
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

There is at least one subarray that it's sum equals to zero.

Have you met this question in a real interview?  
Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        prefix_sum = {0: -1}
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            if sum in prefix_sum:
                return [prefix_sum[sum] + 1, i]
            prefix_sum[sum] = i
        print(prefix_sum)

s = Solution()
print(s.subarraySum([1, 0, 1]))
print(s.subarraySum([1, -1]))
print(s.subarraySum([-3, 1, 2, -3, 4]))
