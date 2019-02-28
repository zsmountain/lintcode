'''
Given an integers array A.

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.Out put B

Have you met this question in a real interview?  
Example
For A = [1, 2, 3], return [6, 3, 2].
'''

class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """

    def productExcludeItself(self, nums):
        # write your code here
        if not nums:
            return []
        product = 1
        res = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            product = product * nums[i - 1]
            res[i] = product
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product = product * nums[i + 1]
            res[i] *= product
        return res

s = Solution()
A = [1, 2, 3]
print(s.productExcludeItself(A))