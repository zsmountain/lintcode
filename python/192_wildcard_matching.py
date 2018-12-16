'''
Description
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Have you met this question in a real interview?  
Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''


class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        # write your code here
        return self.helper(s, 0, p, 0, {})

    def helper(self, s, s_start, p, p_start, memo):
        if (s_start, p_start) in memo:
            return memo[(s_start, p_start)]
        if s_start == len(s):
            return self.is_all_star(p[p_start:])
        if p_start == len(p):
            return s_start == len(s)

        match = True    
        if p[p_start] == '*':
            match = self.helper(s, s_start + 1, p, p_start, memo) or self.helper(s, s_start, p, p_start + 1, memo)
        else:
            match = (p[p_start] == '?' or p[p_start] == s[s_start]) and self.helper(
                s, s_start + 1, p, p_start + 1, memo)

        memo[(s_start, p_start)] = match
        return match
    
    def is_all_star(self, p):
        for c in p:
            if c != '*':
                return False
        return True
        
s = Solution()
print(s.isMatch('abbbaaababbaaabaaabbbabbbbaaabbaaababaabbbbbbaababbabababbababaaabbbbbabababaababaaaaaaabbbaabaabbbaabbabaababbabaababbbabbaaabbbaaaababbaaabbaabaabbbbbaaababaabaabaaabbabaabbbabbbaabbababaabbbbbbbbaaa',
                '*ba***bba*b**abbaa***a*****b*a*bb*b***a*bbb***a***bba*****a****a*a*b**aaaba*aab*a*aa***a*a*b**b**a*b*'))
print(s.isMatch('bbbba', '?*a*a'))
print(s.isMatch('aa', 'a'))
print(s.isMatch('aa', 'aa'))
print(s.isMatch('aaa', 'aa'))
print(s.isMatch('aa', '*'))
print(s.isMatch('aa', 'a*'))
print(s.isMatch('aa', 'a?'))
print(s.isMatch('aab', 'c*a*b'))
