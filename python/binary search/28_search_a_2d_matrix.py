'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Have you met this question in a real interview?  
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
'''

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        row = start if matrix[end][0] > target else end
        start, end = 0, len(matrix[0]) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid
            else:
                 end = mid
        return True if matrix[row][start] == target or matrix[row][end] == target else False

s = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
print(s.searchMatrix(matrix, 3))
print(s.searchMatrix(matrix, 8))