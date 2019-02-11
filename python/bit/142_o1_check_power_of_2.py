'''
Using O(1) time to check whether an integer n is a power of 2.

O(1) 时间复杂度

Have you met this question in a real interview?  
Example
Example 1:
	Input: 4
	Output: true


Example 2:
	Input:  5
	Output: false

Challenge
O(1) time
'''

class Solution:
    """
    @param n: An integer
    @return: True or false
    """

    def checkPowerOf2(self, n):
        # write your code here
        count = 0
        if n <= 0:
            return False
        for i in range(32):
            if n & (1 << i) != 0:
                count += 1
                if count > 1:
                    return False
        return True

s = Solution()
print(s.checkPowerOf2(0))
print(s.checkPowerOf2(4))
print(s.checkPowerOf2(5))