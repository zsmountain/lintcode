'''
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.

Example
For the following binary search tree, in-order traversal by using iterator is [1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12
Challenge
Extra memory usage O(h), h is the height of the tree.

Super Star: Extra memory usage O(1)
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""

from helper import TreeNode, getSampleBstTree

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        if not root:
            self.stack = []
            return
        self.stack = [root]
        while root.left:
            self.stack.append(root.left)
            root = root.left

    """
    @return: True if there has next node, or false
    """

    def hasNext(self, ):
        # write your code here
        return len(self.stack) > 0
    """
    @return: return next node
    """

    def next(self, ):
        # write your code here
        top = self.stack.pop()
        if top.right:
            node = top.right
            self.stack.append(node)
            while node.left:
                self.stack.append(node.left)
                node = node.left
        return top

root = getSampleBstTree()
root.prettyPrint()
s = BSTIterator(root)
while s.hasNext():
    print(s.next().val)


