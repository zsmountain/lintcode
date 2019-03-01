'''
Given a List <Point> p, find the number of (i,j) pairs that satisfy both p[i].x + p[j].x and p[i].y + p[j].y(i < j) can be divisible by 2.

The length of given list len <= 10000.
Have you met this question in a real interview?  
Example
Example1

Input: p = [[1,2],[3,4],[5,6]]
Output: 3
Explanation:
p[0],p[1],p[2] Pairwise Covering, the sum of their x and y can be divided by 2
Example2

Input: p = [[0,3],[1,1],[3,4],[5,6]]
Output: 1
Explanation:
Only when p [2] and p [3] are combined, their sum of x and y can be divided by two.
'''

class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """

    def pairNumbers(self, p):
        # Write your code here
        mapping = {
            (0, 1): 0,
            (1, 1): 0,
            (1, 0): 0,
            (0, 0): 0
        }
        for pair in p:
            mapping[(pair[0] % 2, pair[1] % 2)] = mapping[(pair[0] % 2, pair[1] % 2)] + 1
        return (mapping[(0, 1)] * (mapping[(0, 1)] - 1) + \
            mapping[(1, 0)] * (mapping[(1, 0)] - 1) + \
            mapping[(0, 0)] * (mapping[(0, 0)] - 1) + \
            mapping[(1, 1)] * (mapping[(1, 1)] - 1)) // 2

s = Solution()
print(s.pairNumbers([[1, 2], [3, 4], [5, 6]]))
print(s.pairNumbers([[0, 3], [1, 1], [3, 4], [5, 6]]))
