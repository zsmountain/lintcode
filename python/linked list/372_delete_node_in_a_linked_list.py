'''
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

Have you met this question in a real interview?  
Example
Example 1:

Input:
1->2->3->4->null
3
Output:
1->2->4->null
Example 2:

Input:
1->3->5->null
3
Output:
1->5->null
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
    @param: node: the node in the list should be deletedt
    @return: nothing
    """

    def deleteNode(self, node):
        # write your code here
        node.val = node.next.val
        node.next = node.next.next
