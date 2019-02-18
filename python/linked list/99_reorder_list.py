'''
Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln

reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Have you met this question in a real interview?  
Example
Example 1:
	Input:  1->2->3->4->null
	Output: 1->4->2->3->null

Example 2:
	Input: 1->2->3->4->5->null
	Output: 1->5->2->4->3->null
	
Challenge
Can you do this in-place without altering the nodes' values?
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
    @param head: The head of linked list.
    @return: nothing
    """

    def reorderList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = self.reverseList(slow.next)
        slow.next = None
        dummy = ListNode(0, head)
        while right:
            tmp1 = head.next
            tmp2 = right.next
            head.next = right
            right.next = tmp1
            head = tmp1
            right = tmp2
        
        return dummy.next
        
    def reverseList (self, head):
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

s = Solution()
head = LinkedList([1, 2, 3, 4]).head
head = s.reorderList(head)
printList(head)

head = LinkedList([1, 2, 3, 4, 5]).head
head = s.reorderList(head)
printList(head)
