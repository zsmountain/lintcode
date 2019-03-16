'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Trapping Rain Water

Have you met this question in a real interview?  
Example
Example 1:

Input: [0,1,0]
Output: 0
Example 2:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Challenge
O(n) time and O(1) memory

O(n) time and O(n) memory is also acceptable.
'''

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        # write your code here
        left, right = 0, len(heights) - 1
        left_max = right_max = 0
        res = 0
        while left < right:
            if heights[left] <= heights[right]:
                if heights[left] > left_max:
                     left_max = heights[left]
                else:
                    res += left_max - heights[left]
                left += 1
            else:
                if heights[right] > right_max:
                    right_max = heights[right]
                else:
                    res += right_max - heights[right]
                right -= 1
        return res

s = Solution()
print(s.trapRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
