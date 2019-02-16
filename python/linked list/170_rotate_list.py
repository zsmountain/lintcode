'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Have you met this question in a real interview?  
Example
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):
        # write your code here
        if not head or not k:
            return head
        length = 0
        cur = tail = head
        while cur:
            length += 1
            tail = cur
            cur = cur.next
        k = k % length
        if k == 0: 
            return head
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head
        
        
s = Solution()

head = LinkedList([1, 2, 3, 2, 1]).head
head = s.rotateRight(head, 1)
printList(head)

head = LinkedList([0, 1]).head
head = s.rotateRight(head, 100)
printList(head)

head = LinkedList([1, 2, 3, 4, 5]).head
head = s.rotateRight(head, 2)
printList(head)
