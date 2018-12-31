'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Have you met this question in a real interview?  
Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.

Challenge
The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, n // 2 + 1)
        return (self.findKth(A, B, n // 2) + self.findKth(A, B, n // 2 + 1)) / 2
    
    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        
        a = A[k // 2 - 1] if len(A) >= k // 2 else None
        b = B[k // 2 - 1] if len(B) >= k // 2 else None
        
        if b is None or (a is not None and a < b):
            return self.findKth(A[k // 2:], B, k - k // 2)
        return self.findKth(A, B[k // 2:], k - k // 2)

s = Solution()
A = [1, 2, 3, 4]
B = [5, 6, 7, 8, 9]
print(s.findMedianSortedArrays(A, B))
A = [1, 2, 3, 4, 5, 6]
B = [2, 3, 4, 5]
print(s.findMedianSortedArrays(A, B))
