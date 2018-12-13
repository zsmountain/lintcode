'''
Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. 
Output all possible results.

Have you met this question in a real interview?  
Example
Given the string "123"
return [["1","2","3"],["12","3"],["1","23"]]
'''

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        res = []
        self.helper(s, res, [])
        return res
            
    def helper(self, s, res, cur):
        if len(s) == 0:
            res.append(cur[:])

        for i in range(2):
            if i + 1 <= len(s):
                cur.append(s[:i + 1])
                self.helper(s[i+1:], res, cur)
                cur.pop()

s = Solution()
str = '123'
print(s.splitString(str))