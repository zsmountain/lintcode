'''
Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

Have you met this question in a real interview?  
Example
Given s = "lintcode", dict = ["lint", "code"].

Return true because "lintcode" can be break as "lint code".
'''


class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here
        self.res = False
        self.helper(s, 0, dict, set())
        return self.res

    def helper(self, s, start, dict, memo):
        if self.res == True:
            return
        if start == len(s) or s in memo:
            self.res = True
            return
        for i in range(len(s)):
            if s[start:i+1] in dict:
                memo.add(s[:i+1])
                self.helper(s, i+1, dict, memo)
        
s = Solution()
print(s.wordBreak("cars", ["car", "ca", "rs"]))
print(s.wordBreak('lintcode', ['lint', 'code']))
