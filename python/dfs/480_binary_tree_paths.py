'''
Given a binary tree, return all root-to-leaf paths.

Example
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        res = []
        cur = []
        if not root:
            return res
        self.dfs(root, res, cur)
        return res

    def dfs(self, root, res, cur):
        cur.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(cur))
        if root.left:
            self.dfs(root.left, res, cur)
            cur.pop()
        if root.right:
            self.dfs(root.right, res, cur)
            cur.pop()
        

s = Solution()
root = createTree([1, 2, 3, '#', 5])
print(s.binaryTreePaths(root))
