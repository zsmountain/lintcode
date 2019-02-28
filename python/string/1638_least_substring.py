'''
Given a string containing n lowercase letters, the string needs to be divided into several continuous substrings, the letter in the substring should be same, and the number of letters in the substring does not exceed k, and output the minimal substring number meeting the requirement.

n \leq 1e5n≤1e5
Have you met this question in a real interview?  
Example
Example1

Input: s = "aabbbc", k = 2
Output: 4
Explanation:
we can get "aa", "bb", "b", "c" four substring.
Example2

input: s = "aabbbc", k = 3
Output: 3
we can get "aa", "bbb", "c" three substring.
'''

class Solution:
    """
    @param s: the string s
    @param k: the maximum length of substring
    @return: return the least number of substring
    """
    def getAns(self, s, k):
        # Write your code here
        if not s:
            return 0
        res, count = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1] and count < k:
                count += 1
            else:
                res += 1
                count = 1

        return res

s = Solution()
print(s.getAns('aabbbc', 2))
print(s.getAns('aabbbc', 3))

            
