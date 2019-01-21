'''
Partition an unsorted integer array into three parts:

The front part < low
The middle part >= low & <= high
The tail part > high
Return any of the possible solutions.

low <= high in all testcases.

Have you met this question in a real interview?  
Example
Given [4,3,4,1,2,3,1,2], and low = 2 and high = 3.

Change to [1,1,2,3,2,3,4,4].

([1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not)

Challenge
Do it in place.
Do it in one pass (one loop).
'''

class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """

    def partition2(self, nums, low, high):
        # write your code here
        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] < low:
               nums[i], nums[left] = nums[left], nums[i]
               left += 1
               i += 1
            elif nums[i] > high:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

s = Solution()
nums = [4, 3, 4, 1, 2, 3, 1, 2]
s.partition2(nums, 2, 3)
print(nums)
            
