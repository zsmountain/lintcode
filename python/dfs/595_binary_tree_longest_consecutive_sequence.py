'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Have you met this question in a real interview?  
Example
For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
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

    def longestConsecutive(self, root):
        # write your code here
        self.longest = 0
        self.helper(root)
        return self.longest


    def helper(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = self.helper(root.left)
        right = self.helper(root.right)

        sublongest = 1
        if left and root.val + 1 == root.left.val:
            sublongest = max(sublongest, left + 1)
        if right and root.val + 1 == root.right.val:
            sublongest = max(sublongest, right + 1)

        if sublongest > self.longest:
            self.longest = sublongest

        return sublongest
        

s = Solution()

root = createTree([1, '#', 2, '#', 4, '#', 5, '#', 6])
root.prettyPrint()
print(s.longestConsecutive(root))

root = createTree([1, '#', 3, 2, 4, '#', '#', '#', 5])
root.prettyPrint()
print(s.longestConsecutive(root))
