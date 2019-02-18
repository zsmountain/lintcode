'''
Given a binary search tree and a range [k1, k2], return all elements in the given range.

Have you met this question in a real interview?  
Example
Example 1:

Input:
5
k1 = 6, k2 = 10
Output:
[]
Example 2:

Input:
        20
       /  \
      8   22
     / \
    4   12
k1 = 10, k2 = 22
Output:
[12,20,22]
'''

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import TreeNode, createTree

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        res = []
        self.helper(res, root, k1, k2)
        return res
        
    def helper(self, res, root, k1, k2):
        if not root:
            return
        if root.val < k1:
            self.helper(res, root.right, k1, k2)
        elif root.val > k2:
            self.helper(res, root.left, k1, k2)
        else:
            self.helper(res, root.left, k1, k2)
            res.append(root.val)
            self.helper(res, root.right, k1, k2)

s = Solution()
root = createTree([20, 8, 22, 4, 12])
root.prettyPrint()
print(s.searchRange(root, 10, 22))
        