'''
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

Have you met this question in a real interview?  
Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
return the node 11.
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
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        # write your code here
        self.max_average = -math.inf
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return (0, 0)
        left_count, left_total = self.helper(root.left)
        right_count, right_total = self.helper(root.right)
        count = left_count + right_count + 1
        total = left_total + right_total + root.val
        if total / count > self.max_average:
            self.res = root
            self.max_average = total / count
        return (count, total)

s = Solution()
root = createTree([1, -5, 11, 1, 2, 4, -2])
root.prettyPrint()
print(s.findSubtree2(root).val)

