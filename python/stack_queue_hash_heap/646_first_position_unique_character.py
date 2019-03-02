'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Have you met this question in a real interview?  
Example
Example 1:

Input : s = "lintcode"
Output : 0
Example 2:

Input : s = "lovelintcode"
Output : 2
'''

class Solution:
    """
    @param s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        # write your code here
        mapping = {}
        for ch in s:
            mapping[ch] = mapping.get(ch, 0) + 1
        for i in range(len(s)):
            if mapping[s[i]] == 1:
                return i
        return -1

s = Solution()
print(s.firstUniqChar('lintcode'))
print(s.firstUniqChar('lovelintcode'))
