'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Have you met this question in a real interview?  
Challenge
Could you solve it with O(1) space?
'''

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import ListNode, LinkedList, printList

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        '''
        please see the problme 137 clone graph.
        use the hash map/ dict to mapping the node: new node
        Space: O(n)
        '''
        if not head:
            return None
        #  mapping the node to new node
        mapping = {}
        curr = head
        while curr:
            mapping[curr] = RandomListNode(curr.label)
            curr = curr.next

        #  copy the next and ramdon pointer
        for node in mapping:
            if node.next:
                mapping[node].next = mapping[node.next]
            if node.random:
                mapping[node].random = mapping[node.random]

        return mapping[head]
