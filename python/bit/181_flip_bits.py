'''
Determine the number of bits required to flip if you want to convert integer n to integer m.

Both n and m are 32-bit integers.

Have you met this question in a real interview?  
Example
Given n = 31 (11111), m = 14 (01110), return 2.

Challenge
你能想出几种方法？
'''

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """

    def bitSwapRequired(self, a, b):
        # write your code here
        xor = a^b
        count = 0
        for i in range(32):
            if xor & (1 << i) != 0:
                count += 1
        return count


s = Solution()
print(s.bitSwapRequired(1, -1))
print(s.bitSwapRequired(31, 14))
