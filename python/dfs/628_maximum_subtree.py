'''
Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum sum and the given binary tree is not an empty tree.

Have you met this question in a real interview?  
Example
Example 1:

Input : 
     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5
Output : 3
'''

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import TreeNode, createTree

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import math
class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """

    def findSubtree(self, root):
        # write your code here
        if not root:
            return None
        self.max = -math.inf
        self.node = None
        self.helper(root)
        return self.node

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        sum = left + right + root.val
        if sum > self.max:
            self.max = sum
            self.node = root
        return sum

s = Solution()
root = createTree([1, '#', 2])
print(s.findSubtree(root).val)

root = createTree([1, -5, 2, 0, 3, -4, -5])
print(s.findSubtree(root).val)
