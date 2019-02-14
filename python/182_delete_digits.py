'''
Given string A representative a positive integer which has N digits, remove any k digits of the number, the remaining digits are arranged according to the original order to become a new positive integer.

Find the smallest integer after remove k digits.

N <= 240 and k <= N,

Have you met this question in a real interview?  
Example
Given an integer A = "178542", k = 4

return a string "12"
'''

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """

    def DeleteDigits(self, A, k):
        # write your code here
        A = list(A)
        for i in range(k):
            for j in range(1, len(A)):
                if A[j] < A[j-1]:
                    del A[j-1]
                    break
            else:
                A.pop()
        while len(A) > 1 and A[0] == '0':
            A = A[1:]
        return ''.join(A)

s = Solution()
print(s.DeleteDigits('178542', 4))
