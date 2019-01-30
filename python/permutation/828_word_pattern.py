'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Have you met this question in a real interview?  
Example
Example1

Input:  pattern = "abba" and str = "dog cat cat dog"
Output: true
Explanation:
The pattern of str is abba
Example2

Input:  pattern = "abba" and str = "dog cat cat fish"
Output: false
Explanation:
The pattern of str is abbc
Example3

Input:  pattern = "aaaa" and str = "dog cat cat dog"
Output: false
Explanation:
The pattern of str is abba
Example4

Input:  pattern = "abba" and str = "dog cat cat fish"
Output: false
Explanation:
The pattern of str is abbc
'''

class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """

    def wordPattern(self, pattern, teststr):
        # write your code here
        strs = teststr.split(' ')
        if len(pattern) != len(strs):
            return False
        hash_pattern = {}
        hash_str = {}
        for i in range(len(pattern)):
            if pattern[i] not in hash_pattern:
                hash_pattern[pattern[i]] = strs[i]
            else:
                if hash_pattern[pattern[i]] != strs[i]:
                    return False
            if strs[i] not in hash_str:
                hash_str[strs[i]] = pattern[i]
            else:
                if hash_str[strs[i]] != pattern[i]:
                    return False
        return True