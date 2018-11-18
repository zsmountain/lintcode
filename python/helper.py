class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, l):
        if not l:
            self.head = None
            return
        head = ListNode(l[0])
        pre = head
        for i in range(1, len(l)):
            cur = ListNode(l[i])
            pre.next = cur
            pre = cur
        self.head = head

    def print(self):
        head = self.head
        while head:
            print(head.val, '->', end = ' ')
            head = head.next
        print('None')