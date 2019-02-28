'''
Given two strings, find the longest common substring.

Return the length of it.

The characters in substring should occur continuously in original string. This is different with subsequence.

Have you met this question in a real interview?  
Example
Given A = "ABCD", B = "CBCE", return 2.

Challenge
O(n x m) time and memory.
'''

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """

    def longestCommonSubstring(self, A, B):
        # write your code here
        res = 0
        for i in range(len(A)):
            j = 0
            k = i
            length = 0
            while k < len(A) and j < len(B):
                if A[k] == B[j]:
                    k += 1
                    j += 1
                    length += 1
                else:
                    res = max(res, length)
                    j += 1
                    k = i
                    length = 0
            res = max(res, length)
        return res

s = Solution()
print(s.longestCommonSubstring("adfanadsnf;andvadsjfafjdlsfnaldjfi*odiasjfasdlnfasldgao;inadfjnals;dfjasdl;jfa;dsjfa;sdnfsd;afhwery894yra7f78asfas8fy43rhaisuey34hiuy^%(9afysdfhaksdhfsdkjfhsdhfakldhfsdkf*h",
                               "dafdnf**"))
print(s.longestCommonSubstring('banana', 'cianaic'))
print(s.longestCommonSubstring('ABCD', 'CBCE'))
