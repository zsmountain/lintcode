'''
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.

Have you met this question in a real interview?  
Example
Given [1,2,2,1,3,4,3], return 4

Challenge
One-pass, constant extra space.
'''

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def singleNumber(self, A):
        # write your code here
        res = 0
        for num in A:
            res ^= num
        return res

s = Solution()
print(s.singleNumber([1, 2, 2, 1, 3, 4, 3]))
