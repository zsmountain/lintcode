'''
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word. No same word in dictionary

Have you met this question in a real interview?  
Example
Given matrix:

doaf
agai
dcan
and dictionary:

{"dog", "dad", "dgdg", "can", "again"}

return {"dog", "dad", "can", "again"}

Challenge
Using trie to implement your algorithm.
'''

from helper import Trie

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        # write your code here
        res = []
        if not board or not board[0]:
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.helper(board, words, res, i, j, board[i][j], {(i,j)})
        return res


    def helper(self, board, words, res, i, j, cur, visited):
        if cur in words and not cur in res:
            res.append(cur[:])
        for (x, y, ch) in self.get_next(board, (i,j), visited):
            if (self.is_prefix(words, cur + ch)):
                visited. add((x, y))
                self.helper(board, words, res, x, y, cur + ch, visited)
                visited.remove((x, y))

    def get_next(self, board, point, visited):
        res = []
        x, y = point
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in delta:
            if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]) and not (x+dx, y+dy) in visited:
                res.append((x + dx, y + dy, board[x+dx][y+dy]))
        return res

    def is_prefix(self, words, str):
        for w in words:
            if w.startswith(str):
                return True
        return False

    # use trie
    def wordSearchII(self, board, words):
            # write your code here
        res = []
        if not board or not board[0]:
            return res
        trie = Trie()
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.helper(board, words, res, i, j, board[i][j], {(i, j)}, trie.root.children.get(board[i][j]))
        return res

    def helper(self, board, words, res, i, j, cur, visited, trieNode):
        if not trieNode:
            return
        if trieNode.word and trieNode.word not in res:
            res.append(trieNode.word)
        for (x, y, ch) in self.get_next(board, (i, j), visited):
            visited. add((x, y))
            self.helper(board, words, res, x, y, cur + ch, visited, trieNode.children.get(ch))
            visited.remove((x, y))
    

s = Solution()
print(s.wordSearchII(["aabaab", "bababb", "babbbb",
                      "aababa", "bbaaab", "bbbaba"], ["aaaababab"]))
print(s.wordSearchII(["abce", "sfcs", "adee"], ["see", "se"]))
print(s.wordSearchII(['doaf', 'agai','dcan'], ['dog', 'dad', 'dgdg', 'can', 'again']))
