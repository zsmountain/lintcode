'''
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Have you met this question in a real interview?  
Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge
If the count of numbers is bigger than 2^32, can your code work properly?
'''

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        # write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                left, right = start, mid
                while left + 1 < right:
                    mid = (left + right) // 2
                    if nums[mid] < target:
                        left = mid
                    else:
                        right = mid
                return left if nums[left] == target else right
        return start if nums[start] == target else -1

s = Solution()
nums = [1, 2, 3, 3, 4, 5, 10]
print(s.binarySearch(nums, 1))
print(s.binarySearch(nums, 3))
print(s.binarySearch(nums, 9))
