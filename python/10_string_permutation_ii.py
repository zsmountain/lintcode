'''
Given a string, find all permutations of it without duplicates.

Example
Given "abb", return ["abb", "bab", "bba"].

Given "aabb", return ["aabb", "abab", "baba", "bbaa", "abba", "baab"].
'''

class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        # write your code here
        res = []
        str = sorted(str)
        self.helper(str, res, '')
        return res

    def helper(self, str, res, cur):
        if not str:
            res.append(cur)
            return
        for i, ch in enumerate(str):
            if i > 0 and str[i] == str[i-1]:
                continue
            self.helper(str[:i] + str[i+1:], res, cur + ch)

s = Solution()
print(s.stringPermutation2('abb'))
print(s.stringPermutation2('aabb'))
print(s.stringPermutation2(''))
