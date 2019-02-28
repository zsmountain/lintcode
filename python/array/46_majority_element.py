'''
Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

You may assume that the array is non-empty and the majority number always exist in the array.

Have you met this question in a real interview?  
Example
Example1:
Given [1, 1, 1, 1, 2, 2, 2], return 1
Example2:
Given [1, 1, 1, 2, 2, 2, 2], return 2
Challenge
O(n) time and O(1) extra space
'''

class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums):
        # write your code here
        count = 0
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        return res

s = Solution()
print(s.majorityNumber([2, 1, 2, 1, 2]))
print(s.majorityNumber([1, 1, 1, 1, 2, 2, 2]))
print(s.majorityNumber([1, 1, 1, 2, 2, 2, 2]))
