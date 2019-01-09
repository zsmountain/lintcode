'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


The function prototype should be:

bool isMatch(string s, string p)

Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        # write your code here
        return self.helper(s, 0, p, 0, {})
    
    def helper(self, s, s_start, p, p_start, memo):
        if (s_start, p_start) in memo:
            return memo[(s_start, p_start)]
        if p_start == len(p):
            return s_start == len(s)
        if s_start == len(s):
            p_left = p[p_start:]
            if p_left[-1] != '*':
                return False
            for i in range(len(p_left)):
                if i % 2 == 1 and p_left[i] != '*':
                    return False
            return True
        if (p_start + 1 < len(p) and p[p_start + 1] == '*'):
            match = self.helper(s, s_start, p, p_start + 2, memo) or \
                (self.is_char_match(s[s_start], p[p_start]) and self.helper(s, s_start + 1, p, p_start, memo))
        else:
             match = self.is_char_match(s[s_start], p[p_start]) and self.helper(s, s_start + 1, p, p_start + 1, memo)

        memo[(s_start, p_start)] = match
        return match

    def is_char_match(self, s_char, p_char):
        return s_char == p_char or p_char == '.'
        
s = Solution()
print(s.isMatch('ab', '.*c'))
print(s.isMatch('aa', 'a'))
print(s.isMatch('aa', 'aa'))
print(s.isMatch('aaa', 'aa'))
print(s.isMatch('aa', 'a*'))
print(s.isMatch('aa', '.*'))
print(s.isMatch('ab', '.*'))
print(s.isMatch('aab', 'c*a*b'))
