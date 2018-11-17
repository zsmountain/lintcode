'''
Calculate the a^n % b where a, b and n are all 32bit positive integers.

Example
For 2^31 % 3 = 2

For 100^1000 % 1000 = 0

Challenge
O(logn)
'''

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here
        while (n >= 0):
            if n == 0:
                return 1 % b
            if n == 1:
                return a % b
            product = self.fastPower(a, b, n // 2)
            product = product * product % b
            if n % 2:
                product = product * a % b
            return product % b

s = Solution()
print(s.fastPower(2, 3, 31))
print(s.fastPower(100, 1000, 1000))
print(s.fastPower(3, 7, 5))
