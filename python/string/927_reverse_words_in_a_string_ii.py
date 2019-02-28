'''
Given an input character array, reverse the array word by word. A word is defined as a sequence of non-space characters.

The input character array does not contain leading or trailing spaces and the words are always separated by a single space.

Have you met this question in a real interview?  
Example
Given s = "the sky is blue",
after reversing : "blue is sky the"

Challenge
Could you do it in-place without allocating extra space?
'''

class Solution:
    """
    @param str: a string
    @return: return a string
    """

    def reverseWords(self, str):
        # write your code here
        return " ".join(str.split(' ')[::-1])

s = Solution()
print(s.reverseWords('the sky is blue'))
