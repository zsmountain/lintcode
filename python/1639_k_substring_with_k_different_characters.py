'''
Given a string S and an integer K.
Calculate the number of substrings of length K and containing K different characters

Have you met this question in a real interview?  
Example
String: "abcabc"
K: 3

Answer: 3
substrings:  ["abc", "bca", "cab"]
String: "abacab"
K: 3

Answer: 2
substrings: ["bac", "cab"]
'''

class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        # Write your code here
        res = set()
        hash = set()
        left, right = 0, 0
        while left < len(stringIn):
            while right < len(stringIn) and len(hash) < K:
                if stringIn[right] in hash:
                    break
                hash.add(stringIn[right])
                right += 1
                if len(hash) == K:
                    res.add(stringIn[left:right])
            hash.remove(stringIn[left])
            left += 1
        return len(res)

s = Solution()
print(s.KSubstring('abcabc', 3))
print(s.KSubstring('abacab', 3))
