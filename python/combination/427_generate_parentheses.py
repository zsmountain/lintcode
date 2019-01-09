'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Have you met this question in a real interview?  
Example
Given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """

    def generateParenthesis(self, n):
        # write your code here
        res = []
        self.helper(n, n, res, '')
        return res

    def helper(self, left, right, res, cur):
        if not left and not right:
            res.append(cur)
            return 

        if left >= 0:
            self.helper(left - 1, right, res, cur + '(')
        if right > left:
            self.helper(left, right - 1, res, cur + ')')

s = Solution()
print(s.generateParenthesis(3))
        

