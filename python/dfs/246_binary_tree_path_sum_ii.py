'''
Your are given a binary tree in which each node contains a value. Design an algorithm to get all paths which sum to a given value. The path does not need to start or end at the root or a leaf, but it must go in a straight line down.

Have you met this question in a real interview?  
Example
Given a binary tree:

    1
   / \
  2   3
 /   /
4   2
for target = 6, return

[
  [2, 4],
  [1, 3, 2]
]
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import TreeNode, createTree

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        # write your code here
        res = []
        self.helper(root, target, res, [])
        return res
        

    def helper(self, root, target, res, path):
        if not root:
            return
        path.append(root.val)

        sum = 0
        for i in range(len(path) - 1, -1, -1):
            sum += path[i]
            if sum == target:
                res.append(path[i:])

        self.helper(root.left, target, res, path)
        self.helper(root.right, target, res, path)
        path.pop()

s = Solution()
root = createTree([1, 2, 3, 4, '#', 2])
root.prettyPrint()
print(s.binaryTreePathSum2(root, 6))