'''
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Have you met this question in a real interview?  
Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 1 or 2.

For target = 5, return 4 or 5.

For target = 6, return -1.

Challenge
O(logn) time
'''

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1

s = Solution()
print(s.findPosition([1, 2, 2, 4, 5, 5], 2))
print(s.findPosition([1, 2, 2, 4, 5, 5], 5))
print(s.findPosition([1, 2, 2, 4, 5, 5], 6))

        

