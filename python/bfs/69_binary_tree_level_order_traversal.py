'''
Description
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
 

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.
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

from collections import deque

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        res = []
        if not root:
            return res
        queue = deque([])
        queue.appendleft(root)
        while queue:
            row = []
            for i in range(len(queue)):
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(row)
        return res

s = Solution()
root = createTree([3, 9, 20, '#', '#', 15, 7])
root.prettyPrint()
print(s.levelOrder(root))

root =createTree([1, 2, 3])
root.prettyPrint()
print(s.levelOrder(root))
