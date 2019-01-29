'''
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

Ignore case

Have you met this question in a real interview?  
Example
Given a String CatMat
Given a dictionary ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
return 3

we can form 3 sentences, as follows:
CatMat = Cat Mat
CatMat = Ca tM at
CatMat = C at Mat
'''

class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # Write your code here
        dict = {v.lower() for v in dict}
        s = s.lower()
        return self.helper(s, 0, dict, {})

    def helper(self, s, start, dict, memo):
        if start == len(s):
            return 1
        if s[start:] in memo:
            return memo[s[start:]]
        count = 0
        for i in range(start, len(s)):
            substr = s[start:i+1]
            if substr in dict:
                count += self.helper(s, i+1, dict, memo)
        memo[s[start:]] = count
        return count

s = Solution()
string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(s.wordBreak3(string, dict))
print(s.wordBreak3('CatMat', ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]))
