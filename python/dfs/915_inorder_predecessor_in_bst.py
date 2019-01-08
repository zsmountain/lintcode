'''
Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

If the given node has no in-order predecessor in the tree, return null

Have you met this question in a real interview?  
Example
Given root = {2,1,3}, p = 1, return null.
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
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """

    def inorderPredecessor(self, root, p):
        # write your code here
        pre = None
        while root:
            if root.val >= p.val:
                root = root.left
            else:
                pre = root
                root = root.right
        return pre

s = Solution()
root = createTree([2, 1, 4, '#', '#', 3, 5])
root.prettyPrint()
print(s.inorderPredecessor(root, root).val)
print(s.inorderPredecessor(root, root.left))
print(s.inorderPredecessor(root, root.right).val)
