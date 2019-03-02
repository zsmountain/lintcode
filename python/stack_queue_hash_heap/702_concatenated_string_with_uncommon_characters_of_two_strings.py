'''
Two strings are given and you have to modify 1st string such that all the common characters of the 2nd strings have to be removed and the uncommon characters of the 2nd string have to be concatenated with uncommon characters of the 1st string.

Have you met this question in a real interview?  
Example
Example 1:

Input : s1 = "aacdb", s2 = "gafd"
Output : "cbgf"
Example 2:

Input : s1 = "abcs", s2 = "cxzca"
Output : "bsxz"
'''

class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """

    def concatenetedString(self, s1, s2):
        # write your code here
        mapping = {}
        res = []
        for ch in s1:
            if ch not in mapping:
                mapping[ch] = 1
        for ch in s2:
            if ch in mapping:
                mapping[ch] = 2
        for ch in s1 + s2:
            if mapping.get(ch,0) != 2:
                res.append(ch)
        return ''.join(res)

s = Solution()
print(s.concatenetedString('aacdb', 'gafd'))
print(s.concatenetedString('abcs', 'cxzca'))