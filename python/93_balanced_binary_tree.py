'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
Given binary tree A = {3,9,20,#,#,15,7}, B = {3,#,20,15,7}

A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from helper import TreeNode, createTree

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        self.res = True
        self.helper(root)
        return self.res

    def helper(self, root):
        left_height, right_height = 0, 0
        if root.left:
            left_height = self.helper(root.left)
        if root.right:
            right_height = self.helper(root.right)
        if abs(left_height - right_height) > 1:
            self.res = False
        return 1 + max(left_height, right_height)


s = Solution()

root = createTree([3, 9, 20, '#', '#', 15, 7])
root.prettyPrint()
print(s.isBalanced(root))

root = createTree([3, '#', 20, 15, 7])
root.prettyPrint()
print(s.isBalanced(root))
