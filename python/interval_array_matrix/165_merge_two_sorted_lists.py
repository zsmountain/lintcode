'''
Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.

Have you met this question in a real interview?  
Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
'''
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import ListNode, LinkedList, printList

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummy.next

s = Solution()
l1 = LinkedList([1, 3, 8, 11, 15]).head
l2 = LinkedList([2]).head
head = s.mergeTwoLists(l1, l2)
printList(head)