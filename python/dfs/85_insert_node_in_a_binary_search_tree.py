'''
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

You can assume there is no duplicate values in this tree + node.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  tree = {}, node = 1
	Output:  1
	
	Explanation:
	Insert node 1 into the empty tree, so there is only one node on the tree.

Example 2:
	Input: tree = {2,1,4,3}, node = 6
	Output: {2,1,4,3,6}
	
	Explanation: 
	Like this:



	  2             2
	 / \           / \
	1   4   -->   1   4
	   /             / \ 
	  3             3   6
		
Challenge
Can you do it without recursion?
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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if not root:
            return(node)
        if root.val < node.val:
            root.right = self.insertNode(root.right, node)
        else:
            root.left = self.insertNode(root.left, node)
        return root

s = Solution()
root = createTree([2, 1, 4, '#', '#', 3])
root.prettyPrint()
node = TreeNode(6)
root = s.insertNode(root, node)
root.prettyPrint()
        