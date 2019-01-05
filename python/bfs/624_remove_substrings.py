'''
Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.

Have you met this question in a real interview?  
Example
Given s = ccdaabcdbb, substrs = ["ab", "cd"]
Return 2

Explanation:
ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
'''

from collections import deque
import math

class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s, dict):
        # write your code here
        q = deque([s])
        visited = set()
        res = math.inf
        while q:
            s = q.popleft()
            res = min(res, len(s))
            for substr in dict:
                found = s.find(substr)
                while found != -1:
                    next_string = s[:found] + s[found + len(substr):]
                    if s != next_string and next_string not in visited:
                        q.append(next_string)
                        visited.add(next_string)
                    found = s.find(substr, found + 1)
        return res

s = Solution()
print(s.minLength('abababababababababababaabababababababababababab', set(['ab'])))
print(s.minLength('abcabd', set(['ab', 'abcd'])))
print(s.minLength('ccdaabcdbb', set(['ab', 'cd'])))
