'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

1 -> A
2 -> B
3 -> C
 ...
26 -> Z
27 -> AA
28 -> AB 
Have you met this question in a real interview?  
Example
Example1

Input: 28
Output: "AB"
Example2

Input: 29
Output: "AC"
'''

class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        mapping = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = []
        while n > 0:
            n -= 1
            res.append(mapping[n % 26])
            n //= 26
        res.reverse()
        return ''.join(res)

s = Solution()
print(s.convertToTitle(26))
print(s.convertToTitle(27))
print(s.convertToTitle(28))