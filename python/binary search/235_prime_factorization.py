'''
Prime factorize a given integer.

You should sort the factors in ascending order.

Have you met this question in a real interview?  
Example
Given 10, return [2, 5].

Given 660, return [2, 2, 3, 5, 11].
'''

import math

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        # write your code here
        if num < 2:
            return []
        primes = set()
        res = []
        while True:
            prime = self.getNextPrime(num, primes)
            if prime == num:
                res.append(prime)
                return res
            res.append(prime)
            num //= prime
            
    def getNextPrime(self, num, primes):
        if num in primes:
            return num

        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                primes.add(i)
                return i

        primes.add(num)
        return num

s = Solution()
print(s.primeFactorization(10))
print(s.primeFactorization(60))
print(s.primeFactorization(2))
