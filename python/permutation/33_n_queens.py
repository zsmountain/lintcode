'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Have you met this question in a real interview?  
Example
There exist two distinct solutions to the 4-queens puzzle:

[
  // Solution 1
  [".Q..",
   "...Q",
   "Q...",
   "..Q."
  ],
  // Solution 2
  ["..Q.",
   "Q...",
   "...Q",
   ".Q.."
  ]
]
Challenge
Can you do it without recursion?
'''

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        nums = [str(i) for i in range(n)]
        res = []
        self.dfs(res, '', nums)
        return self.draw_board(res)

    def dfs(self, result, path, nums):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            if not self.is_valid(path, nums[i]):
                continue
            self.dfs(result, path + nums[i], nums[:i] + nums[i+1:])

    def is_valid(self, path, num):
        if num in path:
            return False
        for i in range(len(path)):
            if abs(int(num) - int(path[i])) == abs(len(path)-i):
                return False
        return True
    
    def draw_board(self, res):
        results = []
        for path in res:
            result = []
            for c in path:
                row = ['.'] * len(path)
                row[int(c)] = 'Q'
                result.append(''.join(row))
            results.append(result)
        return results
            
s = Solution()
print(s.solveNQueens(4))

