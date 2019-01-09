'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        # write your code here
        res = []
        self.helper(s, res, [])
        return res

    def helper(self, s, res, cur):
        if len(s) == 0:
            res.append(cur[:])
            return 
        for i in range(len(s)):
            if (self.isPalindrome(s[:i + 1])):
                cur.append(s[:i + 1])
                self.helper(s[i + 1:], res, cur)
                cur.pop()

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

s = Solution()
print(s.partition('aab'))