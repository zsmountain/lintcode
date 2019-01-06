'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

Have you met this question in a real interview?  
Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
 

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        # write your code here
        res = []
        if not root:
            return res

        q = deque([root])
        order = 1
        while q:
            row = []
            for _ in range(len(q)):
                if order == 1:
                    node = q.popleft()
                    row.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    row.append(node.val)
                    if node.right:
                       q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
            order = -order
            res.append(row)
        return res

s = Solution()

root = createTree([1, 2, 3, 4, '#', '#', 5, '#', '#', 6, 7, '#', '#', '#', 8])
root.prettyPrint()
print(s.zigzagLevelOrder(root))

root = createTree([1, 2, '#', '#', 3, 4, 5, '#', '#', 6, 7, 8, 9])
root.prettyPrint()
print(s.zigzagLevelOrder(root))

root = createTree([3, 9, 20, '#', '#', 15, 7])
print(s.zigzagLevelOrder(root))


        
