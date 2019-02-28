'''
Count the number of prime numbers less than a non-negative number, n.

Have you met this question in a real interview?  
Example
Example 1：

Input: n = 2
Output: 0
Example 2：

Input: n = 4
Output: 2
Explanation：2, 3 are prime number
'''

class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        isPrime = [1 for _ in range(n)]
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return sum(isPrime)

s = Solution()
print(s.countPrimes(1500000))
print(s.countPrimes(4))
print(s.countPrimes(5))