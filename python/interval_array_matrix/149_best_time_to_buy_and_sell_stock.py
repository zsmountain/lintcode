'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Have you met this question in a real interview?  
Example
Given array [3,2,3,1,2], return 1.
'''

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        min_val = prices[0]
        res = 0
        for price in prices:
            min_val = min(min_val, price)
            res = max(res, price - min_val)
        return res

s = Solution()
print(s.maxProfit([3, 2, 3, 1, 2]))
