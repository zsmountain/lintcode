'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

You may assume that the array does not change.
There are many calls to sumRange function.
Have you met this question in a real interview?  
Example
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
'''


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = [0]
        sum = 0
        for num in nums:
            sum += num
            self.prefix_sum.append(sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum[j + 1] - self.prefix_sum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
