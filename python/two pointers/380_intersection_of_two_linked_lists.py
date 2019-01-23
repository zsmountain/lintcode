'''
Write a program to find the node at which the intersection of two singly linked lists begins.

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Have you met this question in a real interview?  
Example
The following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Challenge
Your code should preferably run in O(n) time and use only O(1) memory.
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
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # write your code here'
        len_a, len_b = self.get_list_length(headA), self.get_list_length(headB)

        while len_a > len_b:
            headA = headA.next
            len_a -= 1
        while len_b > len_a:
            headB = headB.next
            len_b -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next 
            headB = headB.next
        return None
        

    def get_list_length(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length