'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

Have you met this question in a real interview?  
Example
For n=4, there are 2 distinct solutions.
'''

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):
        # write your code here
        nums = [str(i) for i in range(n)]
        self.res = 0
        self.dfs('', nums)
        return self.res

    def dfs(self, path, nums):
        if not nums:
            self.res += 1
            return
        for i in range(len(nums)):
            if not self.is_valid(path, nums[i]):
                continue
            self.dfs(path + nums[i], nums[:i] + nums[i+1:])

    def is_valid(self, path, num):
        if num in path:
            return False
        for i in range(len(path)):
            if abs(int(num) - int(path[i])) == abs(len(path)-i):
                return False
        return True

s = Solution()
print(s.totalNQueens(4))
print(s.totalNQueens(10))
print(s.totalNQueens(20))
