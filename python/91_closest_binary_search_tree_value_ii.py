'''
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example
Given root = {1}, target = 0.000000, k = 1, return [1].

Challenge
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from helper import TreeNode, getSampleBstTree
from collections import deque

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        # write your code here
        self.prev = deque()
        self.next = deque()
        self.dfs(root, target, k)
        res = []
        for i in range(k):
            if len(self.prev) == 0:
                res.append(self.next.popleft())
                continue
            if len(self.next) == 0:
                res.append(self.prev.pop())
                continue
            res.append(self.prev.pop()) if abs(self.prev[-1] - target) < abs(self.next[0] - target) else res.append(self.next.popleft())
        return res
        
    def dfs(self, root, target, k):
        if not root:
            return
        self.dfs(root.left, target, k)
        if (root.val < target):
            self.prev.append(root.val)
            if len(self.prev) > k:
                self.prev.popleft()
        else:
            self.next.append(root.val)
            if len(self.next) > k:
                self.next.pop()
        if len(self.next) < k:
            self.dfs(root.right, target, k)

s = Solution()
root = getSampleBstTree()
root.prettyPrint()
print(s.closestKValues(root, 8, 4))
