'''
Given a binary tree, return the inorder traversal of its nodes' values.

Have you met this question in a real interview?  
Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
 

return [1,3,2].

Challenge
Can you do it without recursion?
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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        res = []
        s = []
        while root:
            s.append(root)
            root = root.left

        while s:    
            cur = s.pop()
            res.append(cur.val)
            cur = cur.right
            while cur:
                s.append(cur)
                cur = cur.left
            
        return res

s = Solution()
root = createTree([1, 2, 3, 4, 5, 6, 7, 8])
root.prettyPrint()
print(s.inorderTraversal(root))
root = createTree([1, 2, 3, '#', '#', 4, 5])
root.prettyPrint()
print(s.inorderTraversal(root))
