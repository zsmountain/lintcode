'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

Have you met this question in a real interview?  
Example
For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.
'''

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0
        res = max_product = min_product = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            tmp = min_product
            min_product = min(num, min_product * num, max_product * num)
            max_product = max(num, max_product * num, tmp * num)
            res = max(res, max_product)
        return res
s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
