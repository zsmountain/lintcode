'''
There are k sorted arrays nums. Find the median of the given k sorted arrays.

The length of the given arrays may not equal to each other.
The elements of the given arrays are all positive number.
Return 0 if there are no elements in the array.

Example
Given nums = [[1],[2],[3]], return 2.00.
'''

import sys

class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """

    def findMedian(self, nums):
        # write your code here
        total, min_num, max_num = self.getTotalMinMax(nums)
        if not total:
            return 0.0
        if total % 2 != 0:
            return float(self.findKth(nums, min_num, max_num, total // 2.0 + 1))
        return float(self.findKth(nums, min_num, max_num, total // 2) / 2.0 + self.findKth(nums, min_num, max_num, total // 2 + 1) / 2.0)

    def findKth(self, nums, min_num, max_num, k):
        start, end = min_num - 1, max_num + 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.getGreatOrEqualMatrix(nums, mid) < k:
                end = mid
            else:
                start = mid
        if self.getGreatOrEqualMatrix(nums, start) >= k:
            return start
        return end

    def getTotalMinMax(self, nums):
        total, min_num, max_num = 0, sys.maxsize, -sys.maxsize
        for num in nums:
            if not num:
                continue
            total += len(num)
            min_num = min(min_num, num[0])
            max_num = max(max_num, num[-1])
        return (total, min_num, max_num)


    def getGreatOrEqualMatrix(self, nums, val):
        sum = 0
        for num in nums:
            if not num:
                continue
            sum += self.getGreatOrEqualArray(num, val)
        return sum

    def getGreatOrEqualArray(self, nums, val):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < val:
                start = mid
            else:
                end = mid
        if nums[start] >= val:
            return len(nums) - start
        if nums[end] >= val:
            return len(nums) - end
        return 0
            
s = Solution()
print(s.findMedian([[1], [], [2], [3], [3]]))
print(s.findMedian([[1, 20, 300, 401, 502, 6000, 7000]]))
