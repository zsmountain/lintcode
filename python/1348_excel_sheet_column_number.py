'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

Have you met this question in a real interview?  
Example
Example1

Input: "AB"
Output: 28
Example2

Input: "AC"
Output: 29
'''

class Solution:
    """
    @param s: a string
    @return: return a integer
    """

    def titleToNumber(self, s):
        # write your code here
        res = 0
        for ch in s:
            res = res * 26 + (ord(ch) - ord('A') + 1)
        return res

s = Solution()
print(s.titleToNumber('AB'))