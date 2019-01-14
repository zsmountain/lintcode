'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
'''

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if A[m] > B[n]:
                A[i] = A[m]
                m -= 1
            else:
                A[i] = B[n]
                n -= 1
            i -= 1
        while m >= 0:
            A[i] = A[m]
            m -= 1
            i -= 1
        while n >= 0:
            A[i] = B[n]
            n -= 1
            i -= 1

s = Solution()
A = [1, 2, 3, 0, 0]
B = [4, 5]
s.mergeSortedArray(A, 3, B, 2)
print(A)