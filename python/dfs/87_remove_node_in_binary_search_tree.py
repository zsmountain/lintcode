'''
Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.

Have you met this question in a real interview?  
Example
Given binary search tree:

    5
   / \
  3   6
 / \
2   4
Remove 3, you can either return:

    5
   / \
  2   6
   \
    4
or

    5
   / \
  4   6
 /
2
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
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        # write your code here
        if not root:
            return None

        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        else:
            if root.left and root.right:
                max = self.findMax(root)
                root.val = max.val
                root.left = self.removeNode(root.left, max.val)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None

        return root

    def findMax(self, root):
        node = root.left
        while node.right:
            node = node.right
        return node
        
s = Solution()
root = createTree([5, 3, 6, 2, 4])
root = s.removeNode(root, 3)
root.prettyPrint()