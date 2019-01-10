'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

You may assume both pattern and str contains only lowercase letters.

Have you met this question in a real interview?  
Example
Given pattern = "abab", str = "redblueredblue", return true.
Given pattern = "aaaa", str = "asdasdasdasd", return true.
Given pattern = "aabb", str = "xyzabcxzyabc", return false.
'''

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, str):
        # write your code here
        self.res = False
        return self.helper(pattern, str, {}, set())

    def helper(self, pattern, str, mapping, visited):
        if not pattern and not str:
            self.res = True
            return True
        if not pattern or not str:
            return False
        pchar = pattern[0]
        if pchar in mapping:
            if not str.startswith(mapping[pchar]):
                return False
            return self.helper(pattern[1:], str.replace(mapping[pchar], '', 1), mapping, visited)
        for i in range(len(str)):
            substr = str[:i + 1]
            if substr in visited:
                continue

            mapping[pchar] = substr
            visited.add(substr)

            if self.helper(pattern[1:], str.replace(substr, '', 1), mapping, visited):
                return True

            del mapping[pchar]
            visited.remove(substr)
            
        return False
        
s = Solution()
print(s.wordPatternMatch('abba', 'redbluebluered'))
print(s.wordPatternMatch('abab', 'redblueredblue'))
print(s.wordPatternMatch('aaaa', 'asdasdasdasd'))
print(s.wordPatternMatch('aabb', 'xyzabcxzyabc'))
