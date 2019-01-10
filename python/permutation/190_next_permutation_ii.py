'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

Have you met this question in a real interview?  
Example
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

Challenge
The replacement must be in-place, do not allocate extra memory.
'''

class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """

    def nextPermutation(self, nums):
        # write your code here
        i = j = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
            
        while j >= 0 and nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]


s = Solution()
nums = [2, 4, 3, 3, 1]
s.nextPermutation(nums)
print(nums)

nums = [1, 2, 3]
s.nextPermutation(nums)
print(nums)

nums = [1, 3, 2]
s.nextPermutation(nums)
print(nums)

nums = [1, 1, 5]
s.nextPermutation(nums)
print(nums)
