'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Have you met this question in a real interview?  
Example
Example 1:

Input: "([)]"
Output: False
Example 2:

Input: "()[]{}"
Output: True
Challenge
Use O(n) time, n is the number of parentheses.
'''

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        # write your code here
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not self.is_match(top, ch):
                    return False
        return len(stack) == 0

    def is_match(self, ch1, ch2):
        return (ch1 == '(' and ch2 == ')') or (ch1 == '[' and ch2 == ']') or (ch1 == '{' or ch2 == '}')

s = Solution()
print(s.isValidParentheses('([)]'))
print(s.isValidParentheses('()[]{}'))
