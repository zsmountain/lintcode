'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Have you met this question in a real interview?  
Example
Given word1 = "mart" and word2 = "karma", return 3.
'''

class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, word1, word2):
        # write your code here
        return self.helper(word1, word2, len(word1), len(word2), {})
        

    def helper(self, word1, word2, l1, l2, memo):
        if not l1:
            return l2
        if not l2:
            return l1
        if (l1, l2) in memo:
            return memo[(l1, l2)]
        if word1[l1-1] == word2[l2-1]:
            return self.helper(word1, word2, l1 - 1, l2 - 1, memo)
        else:
            res = min(self.helper(word1, word2, l1-1, l2, memo) + 1, self.helper(word1, word2, l1, l2-1, memo) + 1, self.helper(word1, word2, l1-1, l2-1, memo) + 1)
            memo[(l1, l2)] = res
            return res

s = Solution()
print(s.minDistance('mart', 'karma'))