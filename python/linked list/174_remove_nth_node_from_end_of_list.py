'''
Given a linked list, remove the nth node from the end of list and return its head.

The minimum number of nodes in list is n.

Have you met this question in a real interview?  
Example
Example 1:
	Input: list = 1->2->3->4->5->null， n = 2
	Output: 1->2->3->5->null


Example 2:
	Input:  list = 5->4->3->2->1->null, n = 2
	Output: 5->4->3->1->null

Challenge
Can you do it without getting the length of the linked list?
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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        left, right = head, head
        for i in range(n):
            right = right.next
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head

s = Solution()
head = LinkedList([5, 4, 3, 2, 1]).head
head = s.removeNthFromEnd(head, 2)
printList(head)
head = s.removeNthFromEnd(head, 4)
printList(head)