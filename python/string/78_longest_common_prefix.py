'''
Given k strings, find the longest common prefix (LCP).

Have you met this question in a real interview?  
Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"

For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"
'''

class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):
        # write your code here
        res = ''
        if not strs or not strs[0]:
            return res
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != ch:
                    return res
            res += ch
        return res

s = Solution()
print(s.longestCommonPrefix(["ABCDEFG", "ABCEFG", "ABCEFA"]))
            

