'''
Given an unsorted integer array, find the first missing positive integer.

Have you met this question in a real interview?  
Example
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Challenge
Your algorithm should run in O(n) time and uses constant space.
'''

class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """

    def firstMissingPositive(self, A):
        # write your code here
        for i in range(len(A)):
            while 0 < A[i] < len(A) and A[A[i] - 1] != A[i]: 
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
        return len(A) + 1

s = Solution()
print(s.firstMissingPositive([1]))
print(s.firstMissingPositive([3, 4, -1, 1]))