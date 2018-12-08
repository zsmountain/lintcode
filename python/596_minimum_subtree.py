'''
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Have you met this question in a real interview?  
Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 

return the node 1.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import helper
TreeNode = helper.TreeNode

import sys

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        if not root:
            return None
        self.min = sys.maxsize
        self.res = None
        self.dfs(root)
        return self.res

    
    def dfs(self, root):
        if not root:
            return 0
        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)

        tree_sum = left_sum + right_sum + root.val
        if tree_sum < self.min:
            self.min = tree_sum
            self.res = root

        return left_sum + right_sum + root.val
        


treeNode = helper.createTree([1, -5, 2, 0, 2, -4, -5])
s = Solution()
print(s.findSubtree(treeNode).val)
