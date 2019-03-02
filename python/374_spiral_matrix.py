'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Have you met this question in a real interview?  
Example
Example 1:

Input:	[[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2

Input:	[[ 6,4,1 ], [ 7,8,9 ]]
Output: [6,4,1,9,8,7]
'''

class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """

    def spiralOrder(self, matrix):
        # write your code here
        if not matrix:
            return []
        left, up, right, down = 0, 0, len(matrix[0]), len(matrix)
        direction = 0
        res = []
        while True:
            if direction == 0:
                for col in range(left, right):
                    res.append(matrix[up][col])
                up += 1
            elif direction == 1:
                for row in range(up, down):
                    res.append(matrix[row][right - 1])
                right -= 1
            elif direction == 2:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down - 1][col])
                down -= 1
            else:
                for row in range(down - 1, up -1, -1):
                    res.append(matrix[row][left])
                left += 1
            direction = (direction + 1) % 4
            if up >= down or left >= right:
                return res

s = Solution()     
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(s.spiralOrder(matrix))

matrix = [[6, 4, 1],
          [7, 8, 9]]
print(s.spiralOrder(matrix))