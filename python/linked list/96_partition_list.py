'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  list = null, x = 0
	Output: null
	
	Explanation:
	The empty list Satisfy the conditions by itself.

Example 2:
	Input:  list = 1->4->3->2->5->2->null, x = 3
	Output: 1->2->2->4->3->5->null
	
	Explanation:  
	keep the original relative order of the nodes in each of the two partitions.
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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        pre = insert_node = dummy
        while head:
            if head.val < x:
                if insert_node.next != head:
                    pre.next = head.next
                    node = insert_node.next
                    insert_node.next = head
                    head.next = node
                    head = pre.next
                    insert_node = insert_node.next
                else:
                    insert_node = head
                    pre = head
                    head = head.next
            else:
                pre = head
                head = head.next
        return dummy.next

s = Solution()
head = LinkedList([1, 4, 3, 2, 5, 2]).head
#head = LinkedList([3, 3, 1, 2, 4]).head
head = s.partition(head, 3)
printList(head)
	#Input:  list = 1->4->3->2->5->2->null, x = 3
	#Output: 1->2->2->4->3->5->null
