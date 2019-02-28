'''
Given a linked list, swap every two adjacent nodes and return its head.

Have you met this question in a real interview?  
Example
Example 1:

Input: 1->2->3->4->null
Output: 2->1->4->3->null
Example 2:

Input: 5->null
Output: 5->null
Challenge
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
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
    @param head: a ListNode
    @return: a ListNode
    """

    def swapPairs(self, head):
        # write your code here
        dummy = ListNode(0, head)
        cur = dummy
        while cur and cur.next and cur.next.next:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = cur.next.next
            cur.next.next = tmp
            cur = cur.next.next
        return dummy.next

s = Solution()
head = LinkedList([1, 2, 3, 4]).head
printList(s.swapPairs(head))