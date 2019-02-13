'''
Given a list of non negative integers, arrange them such that they form the largest number.

The result may be very large, so you need to return a string instead of an integer.

Have you met this question in a real interview?  
Example
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.

Challenge
Do it in O(nlogn) time complexity.
'''
from functools import cmp_to_key
class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """

    def largestNumber(self, nums):
        # write your code here
        l = [0 for _ in range(10)]
        nums = sorted(nums, key = cmp_to_key(lambda x, y: -1 if str(x) + str(y) > str(y) + str(x) else 1))
        res = ''
        print(nums)
        for num in nums:
            res += str(num)
        if res[0] == '0':
            res = '0'
        return res

s = Solution()
print(s.largestNumber([0, 0]))
print(s.largestNumber([1, 20, 23, 4, 8]))
