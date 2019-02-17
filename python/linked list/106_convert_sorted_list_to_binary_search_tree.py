'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Have you met this question in a real interview?  
Example
               2
1->2->3  =>   / \
             1   3
'''

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import ListNode, LinkedList, printList, TreeNode

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        # write your code here
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        root = TreeNode(mid.val)
        root.right = self.sortedListToBST(mid.next)
        pre.next = None
        root.left = self.sortedListToBST(head)
        return root


s = Solution()
head = LinkedList([1, 2, 3]).head
root = s.sortedListToBST(head)
root.prettyPrint()
