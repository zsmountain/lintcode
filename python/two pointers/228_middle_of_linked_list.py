'''
Find the middle node of a linked list.

Example
Given 1->2->3, return the node with value 2.

Given 1->2, return the node with value 1.

Challenge
If the linked list is in a data stream, can you find the middle without iterating the linked list again?
'''

'''
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
'''


def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))


load_src("helper", "../helper.py")

from helper import LinkedList, ListNode

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if not head:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

for i in range(6):
    ll = LinkedList(range(i))
    ll.print()
    s = Solution()
    mid = s.middleNode(ll.head)
    print(mid.val) if mid else print(None)
