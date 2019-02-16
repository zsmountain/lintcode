'''
Reverse a linked list.

Have you met this question in a real interview?  
Example
Example1:
For linked list 1-> ->3, the reversed linked list is 3->2->1
Example2:
For linked list 1->2->3->4, the reversed linked list is 4->3->2->1

Challenge
Reverse it in-place and in one-pass
'''

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import ListNode, LinkedList, printList

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

s = Solution()
head = LinkedList([1, 2, 3, 4]).head
head = s.reverse(head)
printList(head)
