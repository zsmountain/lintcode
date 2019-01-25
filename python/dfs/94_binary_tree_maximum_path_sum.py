'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Have you met this question in a real interview?  
Example
Given the below binary tree:

  1
 / \
2   3
return 6.
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

import math
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here
        self.res = -math.inf
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.res = max(self.res, left + right + root.val, left + root.val, right + root.val, root.val)
        return max(left + root.val, right + root.val, root.val)

s = Solution()

root = createTree([1, 2, -5, 4, '#', 5, 6])
root.prettyPrint()
print(s.maxPathSum(root))

root = createTree([1, 2, 3])
root.prettyPrint()
print(s.maxPathSum(root))
