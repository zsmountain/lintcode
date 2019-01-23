'''
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

Have you met this question in a real interview?  
Example
Given -21->10->4->5, tail connects to node index 1，return 10
Explanation：
The last node 5 points to the node whose index is 1, which is 10, so the entrance of the ring is 10

Challenge
Follow up:

Can you solve it without using extra space?
'''
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
    @return: The node where the cycle begins. if there is no cycle, return null
    """

    def detectCycle(self, head):
        # write your code here
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if fast and slow == fast:
            while slow != head:
                head = head.next
                slow = slow.next
            return head

        return None
