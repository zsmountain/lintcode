'''
Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

You do not care about the accuracy of the result, we will help you to output results.

Have you met this question in a real interview?  
Example
Given n = 2 return 1.41421356
'''


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        if x < 0:
            raise Exception('Invalid Input!')
        start, end = 0, max(1, x)
        while start + 1e-10 < end:
            mid = (start + end) / 2
            if mid * mid < x:
                start = mid
            elif mid * mid > x:
                end = mid
            else:
                return mid
        return start


s = Solution()
print(s.sqrt(0.000000012))
print(s.sqrt(0.01))
print(s.sqrt(0.1))
print(s.sqrt(2))
print(s.sqrt(3))
print(s.sqrt(4))
print(s.sqrt(5))
print(s.sqrt(10))
