'''
Given two strings, write a method to decide if one is a permutation of the other.

Have you met this question in a real interview?  
Example
abcd is a permutation of bcad, but abbe is not a permutation of abe
'''


class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        # write your code here
        return sorted(A) == sorted(B)