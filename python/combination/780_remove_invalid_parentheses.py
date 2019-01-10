'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

The input string may contain letters other than the parentheses ( and ).

Have you met this question in a real interview?  
Example
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''

class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """

    def removeInvalidParentheses(self, s):
        # Write your code here
        open_left, left, right = 0, 0, 0
        for ch in s:
            if ch == '(':
                left += 1
                open_left += 1
            if ch == ')':
                right += 1
                open_left -= 1
        res = []
        self.helper(s, 0, res, left, right, open_left)
        return res

    def helper(self, s, index, res, left, right, open_left):
        if index == len(s):
            res.append(s)
            return
        for i in range(index, len(s)):
            ch = s[i]
            if open_left <= 0 and ch == ')':
                self.helper(s[:i] + s[i+1:], i, res, left, right - 1, open_left + 1)
            if left > right and ch == '(':
                self.helper(s[:i] + s[i+1:], i, res, left - 1, right, open_left - 1)
            if left < right and ch == ')':
                self.helper(s[:i] + s[i+1:], i, res, left, right - 1, open_left + 1)

s = Solution()
print(s.removeInvalidParentheses('()())()'))
