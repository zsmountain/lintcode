'''
Implement pow(x, n).

You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

Example
Pow(2.1, 3) = 9.261
Pow(0, 1) = 0
Pow(1, 0) = 1

Challenge
O(logn) time

'''

class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if x == 0 and n == 0:
            raise Exception('Invalid input!')
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        product = self.myPow(x, n // 2)
        product *= product
        if (n % 2):
            product = product * x
        return product
            
            
s = Solution()
print(s.myPow(2.1, 3))
print(s.myPow(0, 1))
print(s.myPow(1, 0))
print(s.myPow(3, 5))
print(s.myPow(3, -5))

