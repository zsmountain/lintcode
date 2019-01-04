'''
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Have you met this question in a real interview?  
Example
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
'''

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # write your code here
        res = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                res += 1
                left += 1
                right -= 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1
                while right >= 0 and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1
                while right >= 0 and nums[right] == nums[right + 1]:
                    right -= 1
        return res

s = Solution()
print(s.twoSum6([1, 1, 2, 45, 46, 46], 47))
