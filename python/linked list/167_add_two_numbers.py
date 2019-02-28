'''
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

Have you met this question in a real interview?  
Example
Example 1:
	Input: 7->1->6->null, 5->9->2->null
	Output: 2->1->9->null
	
	Explanation:
	617 + 295 = 912
	912 to list:  2->1->9->null


Example 2:
	Input:  3->1->5->null, 5->9->2->null
	Output: 8->0->8->null
	
	Explanation: 
	513 + 295 = 808
	808 to list: 8->0->8->null
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
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """

    def addLists(self, l1, l2):
        # write your code here
        c = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + c
            if val >= 10:
                val -= 10
                c = 1
            else:
                c = 0
            node = ListNode(val)
            cur.next = node
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if c:
            node = ListNode(c)
            cur.next = node
        return dummy.next

s = Solution()

l1 = LinkedList([9, 9]).head
l2 = LinkedList([9]).head
l = s.addLists(l1, l2)
printList(l)

l1 = LinkedList([7, 1, 6]).head
l2 = LinkedList([5, 9, 3]).head
l = s.addLists(l1, l2)
printList(l)

            
