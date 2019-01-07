'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Have you met this question in a real interview?  
Example
Given root = {1}, target = 4.428571, return 1.
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
from helper import TreeNode

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here
        if not root:
            return None
        return self.dfs(root, target, root.val)
        
    
    def dfs(self, root, target, closest):
        if not root or closest == target:
            return closest
        if abs(root.val - target) <= abs(closest - target):
            closest = root.val
            return self.dfs(root.left, target, closest) if root.val > target else self.dfs(root.right, target, closest)
        else:
            return self.dfs(root.right, target, closest) if closest > target else self.dfs(root.left, target, closest)

s = Solution()
treeNode = helper.getSampleBstTree()
treeNode.prettyPrint()
print(s.closestValue(treeNode, 13.6))
print(s.closestValue(treeNode, 2.7))
print(s.closestValue(treeNode, 5.1))
print(s.closestValue(treeNode, 4.9))
