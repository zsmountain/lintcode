'''
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

The list may contains duplicate integers.

Have you met this question in a real interview?  
Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]

Related Problems
'''


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """

    def nextPermutation(self, nums):
        # write your code here
        i = j = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            nums.reverse()
            return nums

        while j >= 0 and nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]
        return nums