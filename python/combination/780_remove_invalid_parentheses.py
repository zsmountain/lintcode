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
        left, right = 0, 0
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        res = []
        self.helper(s, 0, res, left, right)
        return res

    def helper(self, s, index, res, left, right):
        if left == 0 and right == 0 and self.is_valid(s):
            res.append(s)
            return
        for i in range(index, len(s)):
            if i > index and s[i] == s[i-1]:
                continue
            ch = s[i]
            if left > 0 and ch == '(':
                self.helper(s[:i] + s[i+1:], i, res, left - 1, right)
            if right > 0 and ch == ')':
                self.helper(s[:i] + s[i+1:], i, res, left, right - 1)

    def is_valid(self, s):
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            if ch == ')':
                if count <= 0:
                    return False
                count -= 1
        return count == 0

s = Solution()
print(s.removeInvalidParentheses(')('))
print(s.removeInvalidParentheses('((())))()(('))
print(s.removeInvalidParentheses('()'))
print(s.removeInvalidParentheses('()())()'))
