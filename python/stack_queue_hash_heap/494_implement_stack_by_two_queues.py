'''
Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

Have you met this question in a real interview?  
Example
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
'''

from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.q1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if self.isEmpty():
            raise Exception('pop from empty queue')
        while (len(self.q1) > 1):
            self.q2.append(self.q1.popleft())
        self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if self.isEmpty():
            raise Exception('pop from empty queue')
        while (len(self.q1) > 1):
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()
        self.q2.append(res)
        self.q1, self.q2 = self.q2, self.q1
        return res
    """
    @return: True if the stack is empty
    """

    def isEmpty(self):
        # write your code here
        return len(self.q1) == 0

s = Stack()
s.push(1)
s.pop()
s.push(2)
print(s.isEmpty())
print(s.top())
s.pop()
print(s.isEmpty())
