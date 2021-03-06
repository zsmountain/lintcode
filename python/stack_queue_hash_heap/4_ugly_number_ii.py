'''
Ugly number is a number that only have factors 2, 3 and 5.

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Note that 1 is typically treated as an ugly number.

Example
If n=9, return 10.

Challenge
O(n log n) or O(n) time.
'''

import heapq

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        factors = [2, 3, 5]
        for i in range(n):
            num = heapq.heappop(heap)
            for fac in factors:
                if num * fac not in heap:
                    heapq.heappush(heap, num * fac)
        return num

s = Solution()
print(s.nthUglyNumber(9))



s = Solution()
