'''
Given a string, find the length of the longest substring without repeating characters.

Have you met this question in a real interview?  
Example
Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The longest substring is "abc".
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The longest substring is "b".
Challenge
time complexity O(n)
'''


class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        # write your code here
        j = 0
        res = 0
        chars = set()
        for i in range(len(s)):
            while j < len(s) and s[j] not in chars:
                chars.add(s[j])
                j += 1
            res = max(res, j - i)
            chars.remove(s[i])
        return res

s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))