'''
Given a binary tree, find the length of the longest consecutive sequence path.
The path could be start and end at any node in the tree

Have you met this question in a real interview?  
Example
    1
   / \
  2   0
 /
3
Return 4 // 0-1-2-3
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
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive2(self, root):
        # write your code here
        self.longest = 0
        self.helper(root)
        return self.longest

    def helper(self, root):
        if not root:
            return (0, 0)
        up, down = 0, 0
        left_up, left_down = self.helper(root.left)
        right_up, right_down = self.helper(root.right)
        if root.left:
            if root.val + 1 == root.left.val:
                up = max(up, left_up + 1)
            if root.val - 1 == root.left.val:
                down = max(down, left_down + 1)
        if root.right:
            if root.val + 1 == root.right.val:
                up = max(up, right_up + 1)
            if root.val - 1 == root.right.val:
                down = max(down, right_down + 1)

        self.longest = max(self.longest, up + down + 1)
        return (up, down)

s = Solution()
root = createTree([1, 2, 0, 3])
root.prettyPrint()
print(s.longestConsecutive2(root))