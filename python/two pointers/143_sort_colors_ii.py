'''
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

You are not suppose to use the library's sort function for this problem.

k <= n

Have you met this question in a real interview?  
Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?
'''


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        self.quickSort(colors, k, 0, len(colors) - 1, 0, k)
    
    def quickSort(self, colors, k, colors_start, colors_end, k_start, k_end):
        if colors_start >= colors_end or k_start >= k_end:
            return
        left, right = colors_start, colors_end
        pivot = (k_start + k_end) // 2
        while left <= right:
            while left <= right and colors[left] <= pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
                
        self.quickSort(colors, k, colors_start, right, k_start, pivot)
        self.quickSort(colors, k, left, colors_end, pivot + 1, k_end)

s = Solution()
nums = [3, 2, 2, 1, 4]
s.sortColors2(nums, 4)
print(nums)