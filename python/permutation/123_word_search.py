'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Have you met this question in a real interview?  
Example
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        # write your code here
        if not word or not board or not board[0]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, set([(i, j)])):
                    return True
        return False

    def helper(self, board, x, y, word, visited):
        if len(word) == 1 and board[x][y] == word[0]:
            return True
        if board[x][y] != word[0]:
            return False
        delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dx, dy in delta:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                if self.helper(board, next_x, next_y, word[1:], visited):
                    return True
                else:
                    visited.remove((next_x, next_y))
        return False

s = Solution()

board = ['z']
print(s.exist(board, 'z'))

board = [
    'ABCE',
    'SFCS',
    'ADEE'
]
print(s.exist(board, 'ABCCED'))
print(s.exist(board, 'SEE'))
print(s.exist(board, 'ABCB'))
