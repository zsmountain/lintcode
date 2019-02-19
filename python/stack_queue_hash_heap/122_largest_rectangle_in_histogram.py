'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

histogram

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

histogram

The largest rectangle is shown in the shaded area, which has area = 10 unit.
'''

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    def largestRectangleArea(self, height):
        # write your code here
        stack = []
        res = 0
        for i, h in enumerate(height + [0]):
            while stack and height[stack[-1]] >= h:
                index = stack.pop()
                left = stack[-1] if stack else -1
                res = max(res, height[index] * (i - left - 1))
            stack.append(i)
        return res

s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
