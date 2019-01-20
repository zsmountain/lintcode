'''
Implement int sqrt(int x).

Compute and return the square root of x.

Have you met this question in a real interview?  
Example
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3


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
        if x < 2:
            return x
        start, end = 1, x
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid < x:
                start = mid
            elif mid * mid > x:
                end = mid
            else:
                return mid
        if end * end < x:
            return end
        else:
            return start

s = Solution()
print(s.sqrt(2147483647))
print(s.sqrt(3))        
print(s.sqrt(4))        
print(s.sqrt(5))        
print(s.sqrt(10))        
