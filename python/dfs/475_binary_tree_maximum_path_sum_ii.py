'''
Given a binary tree, find the maximum path sum from root.

The path may end at any node in the tree and contain at least one node in it.

Have you met this question in a real interview?  
Example
Given the below binary tree:

  1
 / \
2   3
return 4. (1->3)
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
    @param root: the root of binary tree.
    @return: An integer
    """

    def maxPathSum2(self, root):
        # write your code here
        if not root:
            return 0
        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)
        return max(left + root.val, right + root.val, root.val)

s = Solution()

root = createTree([-1, -3, -7])
root.prettyPrint()
print(s.maxPathSum2(root))

root = createTree([1, 2, 3])
root.prettyPrint()
print(s.maxPathSum2(root))
