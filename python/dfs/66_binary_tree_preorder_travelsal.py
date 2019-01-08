'''
Given a binary tree, return the preorder traversal of its nodes' values.

Have you met this question in a real interview?  
Example
Given:

    1
   / \
  2   3
 / \
4   5
return [1,2,4,5,3].
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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        res = []
        if not root:
            return []
        s = [root]
        while s:
            cur = s.pop()
            res.append(cur.val)
            if cur.right:
                s.append(cur.right)
            if cur.left:
                s.append(cur.left)
        return res

s = Solution()
root = createTree([1, 2, 3, 4, 5, 6, 7, 8])
root.prettyPrint()
print(s.preorderTraversal(root))
root = createTree([1, 2, 3, '#', '#', 4, 5])
root.prettyPrint()
print(s.preorderTraversal(root))
