'''
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Have you met this question in a real interview?  
Example
Given lists:

[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

from helper import ListNode, printList
import heapq

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        heap = []
        sequence = 1
        for node in lists:
            while node:
                heapq.heappush(heap, (node.val, sequence, node))
                sequence += 1
                node = node.next
        if not heap:
            return None
        pre = dummy = ListNode(-1)
        while heap:
            val, sequence, node = heapq.heappop(heap)
            pre.next = node
            pre = node
        return dummy.next

s = Solution()

node = ListNode(1)
head = s.mergeKLists([node])
printList(head)

node4 = ListNode(4)
node2 = ListNode(2, node4)
node1 = ListNode(-1)
head = s.mergeKLists([node2, None, node1])
printList(head)
