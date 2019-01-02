'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return 2147483647

Have you met this question in a real interview?  
Example
Given dividend = 100 and divisor = 9, return 11.
'''

class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """

    def divide(self, dividend, divisor):
        # write your code here
        if divisor == 0:
            return 2147483647

        sign = 1
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            sign = -1
        divisor = abs(divisor)
        dividend = abs(dividend)

        if divisor > dividend:
            return 0

        cnt = 1
        res = 0

        a = dividend
        b = divisor
        while a >= b:
            b += b
            if a >= b:
                cnt += cnt
            else:
                res += cnt
                cnt = 1
                b = b >> 1
                a = a - b
                b = divisor

        return 2147483647 if res * sign > 2147483647 else res * sign

s = Solution()
print(s.divide(-1, -1))
print(s.divide(100, 9))
            
        

        
        
        
