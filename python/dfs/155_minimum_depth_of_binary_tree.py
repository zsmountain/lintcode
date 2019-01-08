'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Have you met this question in a real interview?  
Example
Given a binary tree as follow:

  1
 / \ 
2   3
   / \
  4   5  
The minimum depth is 2.
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
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        self.min = math.inf
        self.helper(root, 1)
        return self.min
    
    def helper(self, root, height):
        if not root.left and not root.right:
            self.min = min(self.min, height)
            return

        if root.left:
            self.helper(root.left, height + 1)
        if root.right:
            self.helper(root.right, height + 1)

s = Solution()
root = createTree([1, '#', 2, 3])
print(s.minDepth(root))
root = createTree([1, 2, 3, '#', '#', 4, 5])
print(s.minDepth(root))
