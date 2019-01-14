'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example
Given root = {1,#,2}, k = 2, return 2.

Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
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
from helper import TreeNode, getSampleBstTree

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        self.res = None
        self.count = k
        self.dfs(root)
        return self.res
        
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.count -= 1
        if self.count == 0:
            self.res = root.val
            return
        self.dfs(root.right)

s = Solution()
root = getSampleBstTree()
root.prettyPrint()
print(s.kthSmallest(root, 1))
print(s.kthSmallest(root, 2))
