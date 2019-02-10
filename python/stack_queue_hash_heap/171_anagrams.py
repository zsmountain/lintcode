'''
Given an array of strings, return all groups of strings that are anagrams.

All inputs will be in lower-case

Have you met this question in a real interview?  
Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Challenge
What is Anagram?

Two strings are anagram if they can be the same after change the order of characters.
'''

class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        hash = {}
        res = []
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in hash:
                hash[sorted_str].append(s)
            else:
                hash[sorted_str] = [s]
        for vals in hash.values():
            if len(vals) >= 2:
                res += vals
        return res

s = Solution()
print(s.anagrams(["lint", "intl", "inlt", "code"]))
