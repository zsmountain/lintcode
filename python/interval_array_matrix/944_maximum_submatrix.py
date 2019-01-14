'''
Given an n x n matrix of positive and negative integers, find the submatrix with the largest possible sum.

Have you met this question in a real interview?  
Example
Given matrix = 
[
[1,3,-1],
[2,3,-2],
[-1,-2,-3]
]
return 9.
Explanation:
the submatrix with the largest possible sum is:
[
[1,3],
[2,3]
]
'''

import sys

class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        maxSum = - sys.maxsize
        rows, columns = len(matrix), len(matrix[0])
        for topRow in range(rows):
            compressedRow = [0] * columns
            for row in range(topRow, rows):
                minSum, nextPrefixSum = 0, 0
                for col in range(columns):
                    compressedRow[col] += matrix[row][col]
                    nextPrefixSum += compressedRow[col]
                    maxSum = max(maxSum, nextPrefixSum - minSum)
                    minSum = min(minSum, nextPrefixSum)

        return maxSum

s = Solution()
print(s.maxSubmatrix([
    [41, 48, 9, -70], 
    [91, -99, 54, -19],
    [17, -86, -70, -26], 
    [-15, 31, -53, -38]]))

print(s.maxSubmatrix([
    [1, 3, -1],
    [2, 3, -2],
    [-1, -2, -3]
]))
