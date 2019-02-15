'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  null
	Output: null


Example 2:
	Input:  1->1->2->null
	Output: 1->2->null
	
Example 3:
	Input:  1->1->2->->3->3->null
	Output: 1->2->3->null
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
    @param head: head is the head of the linked list
    @return: head of linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return head
        pre = head
        cur = head.next
        while cur:
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head

s = Solution()
head = LinkedList([1, 1, 2, 3, 3]).head
head = s.deleteDuplicates(head)
printList(head)

