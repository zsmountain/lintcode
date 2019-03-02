'''
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.

If the "compressed" string would not become smaller than the original string, your method should return the original string.

You can assume the string has only upper and lower case letters (a-z).

Have you met this question in a real interview?  
Example
Example 1:

Input: str = "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:

Input: str = "aabbcc"
Output: "aabbcc"
'''

class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """

    def compress(self, originalString):
        # write your code here
        res = []
        cur = None
        count = 0
        for ch in originalString:
            if not cur:
                cur = ch
                count = 1
                continue
            if cur == ch:
                count += 1
            else:
                res.append(cur)
                res.append(str(count))
                cur = ch
                count = 1
        res.append(cur)
        res.append(str(count))
        if len(originalString) > len(res):
            return ''.join(res)
        else:
            return originalString

s = Solution()
print(s.compress('aabcccccaaa'))
print(s.compress('aabbcc'))
