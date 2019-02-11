'''
Write an algorithm which computes the number of trailing zeros in n factorial.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  11
	Output: 2
	
	Explanation: 
	11! = 39916800, so the output should be 2

Example 2:
	Input:  5
	Output: 1
	
	Explanation: 
	5! = 120, so the output should be 1.

Challenge
O(log N) time
'''

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        res = 0
        while n:
            n //= 5
            res += n
        return res

s = Solution()
print(s.trailingZeros(11))
print(s.trailingZeros(5))