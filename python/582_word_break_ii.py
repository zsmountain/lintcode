'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Have you met this question in a real interview?  
Example
Gieve s = lintcode,
dict = ["de", "ding", "co", "code", "lint"].

A solution is ["lint code", "lint co de"].
'''

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []

        if s in wordDict:
            partitions.append(s)
            
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            sub_partitions = self.helper(s[i:], wordDict, memo)
            for sub_partition in sub_partitions:
                partitions.append(prefix + " " + sub_partition)

        memo[s] = partitions
        return partitions

s = Solution()
print(s.wordBreak('aaaaaaaaaaaaabaaaaaaaaaaa', ["a", "aa", "aaa", "aaaa", "aaaaa"]))
print(s.wordBreak('lintcode', ["de", "ding", "co", "code", "lint"]))
