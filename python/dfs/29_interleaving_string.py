'''
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.

Have you met this question in a real interview?  
Example
Example 1:

Input:
"aabcc"
"dbbca"
"aadbbcbcac"
Output:
true
Example 2:

Input:
""
""
"1"
Output:
false
Example 3:

Input:
"aabcc"
"dbbca"
"aadbbbaccc"
Output:
false
Challenge
O(n2) time or better
'''

class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        # write your code here
        return self.helper(s1, s2, s3, 0, 0, 0)

    def helper(self, s1, s2, s3, i1, i2, i3):
        if i3 == len(s3):
            return True
        if i1 == len(s1):
            return s2[i2:] == s3[i3:]
        if i2 == len(s2):
            return s1[i1:] == s3[i3:]
        if s1[i1] != s3[i3] and s2[i2] != s3[i3]:
            return False
        return self.helper(s1, s2, s3, i1 + 1, i2, i3 + 1) or self.helper(s1, s2, s3, i1, i2 + 1, i3 + 1)
            
s = Solution()
print(s.isInterleave("aabcc",
                     "dbbca",
                     "aadbbcbcac"))
