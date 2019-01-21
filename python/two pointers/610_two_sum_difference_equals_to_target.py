'''
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

It's guaranteed there is only one available solution

Have you met this question in a real interview?  
Example
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)
'''

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum7(self, nums, target):
        # write your code here
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        left, right = 0, 1
        target = abs(target)
        while right < len(nums):
            if left == right:
                right += 1
                continue
            if nums[right][0] - nums[left][0] < target:
                right += 1
            elif nums[right][0] - nums[left][0] > target:
                left += 1
            else:
                return sorted([nums[left][1] + 1, nums[right][1] + 1])

s = Solution()
nums = [1, 0, -1]
print(s.twoSum7(nums, -2))
nums = [1, 0, 1]
print(s.twoSum7(nums, 0))
