'''
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Example
push(1)
pop()     // return 1
push(2)
push(3)
top()     // return 2
pop()     // return 2
Challenge
implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.
'''

class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.s1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            raise Exception('pop from empty q')
        return self.s2.pop()
    """
    @return: An integer
    """

    def top(self):
        # write your code here
        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            raise Exception('pop from empty q')
        return self.s2[-1]

q = MyQueue()
q.push(1)
print(q.pop())
q.push(2)
q.push(3)
print(q.top())
print(q.pop())
