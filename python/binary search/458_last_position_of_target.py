'''
Find the last position of a target number in a sorted array. Return -1 if target does not exist.

Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 2.

For target = 5, return 5.

For target = 6, return -1.
'''

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

s = Solution()
print(s.lastPosition([1, 2, 2, 4, 5, 5], 2))
print(s.lastPosition([1, 2, 2, 4, 5, 5], 5))
print(s.lastPosition([1, 2, 2, 4, 5, 5], 6))
print(s.lastPosition([], 6))
