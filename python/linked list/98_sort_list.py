'''
Sort a linked list in O(n log n) time using constant space complexity.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  1->3->2->null
	Output:  1->2->3->null

Example 2:
	Input: 1->7->2->6->null
	Output: 1->2->6->7->null
	
Challenge
Solve it by merge sort & quick sort separately.
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
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        while left:
            cur.next = left
            left = left.next
            cur = cur.next
        while right:
            cur.next = right
            right = right.next
            cur = cur.next
        return dummy.next

    def get_mid(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow

s = Solution()
head = LinkedList([1, 3, 2]).head
head = s.sortList(head)
printList(head)

head = LinkedList([1, 7, 2, 6]).head
head = s.sortList(head)
printList(head)
