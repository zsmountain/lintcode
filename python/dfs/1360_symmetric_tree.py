'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Have you met this question in a real interview?  
Example
Example1

Input: {1,2,2,3,4,4,3}
Output: true
Explanation:
    1
   / \
  2   2
 / \ / \
3  4 4  3
This binary tree {1,2,2,3,4,4,3} is symmetric
Example2

Input: {1,2,2,#,3,#,3}
Output: false
Explanation:
    1
   / \
  2   2
   \   \
   3    3
This is not a symmetric tree
Challenge
Could you solve it both recursively and iteratively?
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
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """

    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)

s = Solution()
root = createTree([1, 2, 2, 3, 4, 4, 3])
root.prettyPrint()
print(s.isSymmetric(root))
