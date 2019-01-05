'''
Find the kth smallest number in an unsorted integer array.

Have you met this question in a real interview?  
Example
Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers is 3.

Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
'''

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        # write your code here
        return self.helper(k, nums, 0, len(nums) - 1)

    def helper(self, k, nums, start, end):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if right - start + 1 >= k:
            return self.helper(k, nums, start, right)
        if left - start + 1 <= k:
            return self.helper(k - (left - start), nums, left, end) 
        return nums[right + 1]

s = Solution()
print(s.kthSmallest(3, [3, 4, 1, 2, 5]))