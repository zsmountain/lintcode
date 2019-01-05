'''
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

Have you met this question in a real interview?  
Example
Given binary tree:

    1
   / \
  2   3
 /
4
return

[
  1->null,
  2->3->null,
  4->null
]
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")

from helper import TreeNode, createTree, ListNode, printList

from collections import deque
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            head, previous = None, None
            for _ in range(len(q)):
                treeNode = q.popleft()
                listNode = ListNode(treeNode.val)
                if not head:
                    head = listNode
                if previous:
                    previous.next = listNode
                previous = listNode
                
                if treeNode.left:
                    q.append(treeNode.left)
                if treeNode.right:
                    q.append(treeNode.right)
            res.append(head)
        return res

s = Solution()
root = createTree([1, 2, 3, 4])
res = s.binaryTreeToLists(root)
for head in res:
    printList(head)
                

