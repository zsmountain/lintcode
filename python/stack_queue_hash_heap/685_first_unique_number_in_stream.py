'''
Given a continuous stream of numbers, write a function that returns the first unique number whenever terminating number is reached(include terminating number). If there no unique number before terminating number or you can't find this terminating number, return -1.

Have you met this question in a real interview?  
Example
Given a stream [1, 2, 2, 1, 3, 4, 4, 5, 6] and a number 5
return 3

Given a stream [1, 2, 2, 1, 3, 4, 4, 5, 6] and a number 7
return -1
'''

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head
        self.val_to_prev_node_map = {}
        self.duplicates = set()

    def add(self, num):
        if num in self.duplicates:
            return
        if num in self.val_to_prev_node_map:
            self.remove(num)
            self.duplicates.add(num)
        else:
            node = ListNode(num)
            self.val_to_prev_node_map[num] = self.tail
            self.tail.next = node
            self.tail = node

    def remove(self, num):
        prev = self.val_to_prev_node_map[num]
        prev.next = prev.next.next
        del self.val_to_prev_node_map[num]

        if prev.next:
            self.val_to_prev_node_map[prev.next.val] = prev
        else:
            self.tail = prev
            
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        # Write your code here
        linkedList = LinkedList()
        for num in nums:
            linkedList.add(num)
            if num == number:
                return linkedList.head.next.val if linkedList.head else -1
        return -1

s = Solution()
print(s.firstUniqueNumber([1, 2, 2, 1, 2, 4, 4, 5, 6, 5, 7, 6, 8], 8))
print(s.firstUniqueNumber([1, 2, 2, 1, 3, 4, 4, 5, 6], 3))
print(s.firstUniqueNumber([1, 2, 2, 1, 3, 4, 4, 5, 6], 5))
print(s.firstUniqueNumber([1, 2, 2, 1, 3, 4, 4, 5, 6], 7))
