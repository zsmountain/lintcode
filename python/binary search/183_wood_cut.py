'''
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.

Have you met this question in a real interview?  
Example
For L=[232, 124, 456], k=7, return 114.

Challenge
O(n log Len), where Len is the longest length of the wood.
'''

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        start, end = 0, sum(L)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_cut_count(L, mid) >= k:
                start = mid
            else:
                end = mid
        return end if self.get_cut_count(L, end) >= k else start
                

    def get_cut_count(self, L, length_per_piece):
        res = 0
        for length in L:
            res += length // length_per_piece
        return res

s = Solution()
L = [232, 124, 456]
k = 7
print(s.woodCut(L, k))
