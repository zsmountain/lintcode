'''
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

The characters of B in A are not necessary continuous or ordered.

Have you met this question in a real interview?  
Example
For A = "ABCD", B = "ACD", return true.

For A = "ABCD", B = "AABC", return false.
'''

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # write your code here
        hash = {}
        for ch in A:
            hash[ch] = hash.get(ch, 0) + 1
        for ch in B:
            hash[ch] = hash.get(ch, 0) - 1
        for val in hash.values():
            if val < 0:
                return False
        return True

s = Solution()
print(s.compareStrings('ABCD', 'ACD'))
print(s.compareStrings('ABCD', 'AABC'))