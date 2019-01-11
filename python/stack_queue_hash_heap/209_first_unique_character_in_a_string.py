'''
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

Have you met this question in a real interview?  
Example
For "abaccdeff", return 'b'.

Challenge
不使用额外的存储空间。
'''

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here
        map = {}
        for ch in str:
            map[ch] = map.get(ch, 0) + 1
        for ch in str:
            if map[ch] == 1:
                return ch

s = Solution()
print(s.firstUniqChar('abaccdeff'))
