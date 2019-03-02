'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Have you met this question in a real interview?  
Example
Example 1：

Input:[[1,2],[3,4]]
Output:[[3,1],[4,2]]
Example 2:

Input:[[1,2,3],[4,5,6],[7,8,9]]
Output:[[7,4,1],[8,5,2],[9,6,3]]
Challenge
Do it in-place.
'''

class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """

    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

s = Solution()
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
s.rotate(matrix)
print(matrix)
matrix = [[1, 2],
          [3, 4]]
s.rotate(matrix)
print(matrix)
