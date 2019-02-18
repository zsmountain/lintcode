'''
Given preorder and inorder traversal of a tree, construct the binary tree.

You may assume that duplicates do not exist in the tree.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  [], []
	Output: null  


Example 2:
	Input: in-order = [1,2,3], pre-order = [2,1,3]
	Output:  
	
	  2
	 / \
	1   3
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


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """

    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 0
        while inorder[i] != preorder[0]:
            i += 1
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root

s = Solution()
#root = s.buildTree([1, 2, 3], [2, 1, 3])
root = s.buildTree([6, 2, 3, 4, 5], [2, 4, 5, 3, 6])
root.prettyPrint()