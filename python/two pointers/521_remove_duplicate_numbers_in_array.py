'''
Given an array of integers, remove the duplicate numbers in it.

You should:

Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.
You don't need to keep the original order of the integers.

Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.
'''

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
        nums.sort()
        
        res = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[res] = nums[i]
                res += 1

        return res


s = Solution()
nums = [1, 3, 1, 4, 4, 2]
print(s.deduplication(nums))
print(nums)
