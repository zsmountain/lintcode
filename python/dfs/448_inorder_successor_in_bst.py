'''
Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return null.

It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)

Have you met this question in a real interview?  
Example
Given tree = [2,1] and node = 1:

  2
 /
1
return node 2.

Given tree = [2,1,3] and node = 2:

  2
 / \
1   3
return node 3.

Challenge
O(h), where h is the height of the BST.
'''

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import TreeNode, createTree

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        sucessor = None
        while root:
            if root.val > p.val:
                sucessor = root
                root = root.left
            elif root.val <= p.val:
                root = root.right
                
        return sucessor

s = Solution()
root = createTree([2, 1, 4, '#', '#', 3, 5])
root.prettyPrint()
print(s.inorderSuccessor(root, root).val)
print(s.inorderSuccessor(root, root.left).val)
print(s.inorderSuccessor(root, root.right).val)
