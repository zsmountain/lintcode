'''
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Have you met this question in a real interview?  
Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
Challenge
Do it in-place without any extra memory.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from helper import TreeNode, createTree

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        # write your code here
        if not root:
            return None
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return
        elif not root.left:
            self.dfs(root.right)
        elif not root.right:
            root.right = root.left
            root.left = None
            self.dfs(root.right)
        else:
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            root.right = root.left
            root.left = None
            self.dfs(root.right)


s = Solution()

root = createTree([7, -10, 2, -4, 3, -8, '#', '#', '#', '#', -1, 11])
root.prettyPrint()
s.flatten(root)
root.prettyPrint()

root = createTree([1, 2, 5, 3, 4, '#', 6])
root.prettyPrint()
s.flatten(root)
root.prettyPrint()

