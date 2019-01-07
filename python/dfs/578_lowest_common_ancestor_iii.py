'''
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.

node A or node B may not exist in tree.

Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import TreeNode, createTree

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        found_a, found_b, lca = self.helper(root, A, B)
        if not found_a or not found_b:
            return None
        return lca

    def helper(self, root, A, B):
        if not root:
            return False, False, None
        found_a_left, found_b_left, left_lca = self.helper(root.left, A, B)
        found_a_right, found_b_right, right_lca =self.helper(root.right, A, B)

        found_a = found_a_left or found_a_right or A == root
        found_b = found_b_left or found_b_right or B == root
        
        if A == root or B == root:
            return found_a, found_b, root
        if left_lca and right_lca:
            return found_a, found_b, root
        if left_lca:
            return found_a, found_b, left_lca
        if right_lca:
            return found_a, found_b, right_lca
        return found_a, found_b, None

s = Solution()
root = createTree([4, 3, 7, '#', '#', 5, 6])
node3 = root.left
node7 = root.right
node5 = node7.left
node6 = node7.right
print(s.lowestCommonAncestor3(root, node3, node5).val)
print(s.lowestCommonAncestor3(root, node5, node6).val)
print(s.lowestCommonAncestor3(root, node6, node7).val)
print(s.lowestCommonAncestor3(root, node6, TreeNode(1)))
