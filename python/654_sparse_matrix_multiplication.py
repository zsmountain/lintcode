'''
Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        # write your code here
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        m, n, k = len(A), len(A[0]), len(B[0])
        res = [[0 for i in range(k)] for j in range(m)]
        for i in range(m):
            for j in range(k):
                for l in range(n):
                    res[i][j] += A[i][l] * B[l][j]
        return res

    def multiply(self, A, B):
        # write your code here
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        m, n, k = len(A), len(A[0]), len(B[0])
        res = [[0 for i in range(k)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    continue
                for l in range(k):
                    res[i][l] += A[i][j] * B[j][l]
        return res

s = Solution()
A = [
    [1, 0, 0],
    [-1, 0, 3]
]

B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]
print(s.multiply(A, B))


