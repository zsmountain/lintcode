'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  []
	Output: 0


Example 2:
	Input:  [1,1,2]
	Output: 2
	
	Explanation:  
	uniqued array: [1,2]
'''

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        if not nums:
            return 0
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1

s = Solution()
print(s.removeDuplicates([1, 1, 1, 1, 2, 2, 2]))
