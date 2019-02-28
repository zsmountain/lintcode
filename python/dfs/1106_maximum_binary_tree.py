'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

The size of the given array will be in the range [1,1000].

Have you met this question in a real interview?  
Example
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
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
    @param nums: an array
    @return: the maximum tree
    """

    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, start, end):
        if not nums or start > end:
            return None
        pos, val = self.findMax(nums, start, end)
        root = TreeNode(val)
        root.left = self.dfs(nums, start, pos-1)
        root.right = self.dfs(nums, pos+1, end)
        return root

    def findMax(self, nums, start, end):
        pos, val = start, nums[start]
        for i in range(start, end + 1):
            if nums[i] > val:
                pos, val = i, nums[i]
        return (pos, val)

s = Solution()
root = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
root.prettyPrint()
