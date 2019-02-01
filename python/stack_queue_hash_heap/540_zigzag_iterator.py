'''
Given two 1d vectors, implement an iterator to return their elements alternately.

Have you met this question in a real interview?  
Example
Given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
'''

from collections import deque

class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.q1 = deque(v1)
        self.q2 = deque(v2)
        self.isq1 = True
    
    """
    @return: An integer
    """
    def next(self):
        # write your code here
        if self.q1 and self.q2:
            res = self.q1.popleft() if self.isq1 else self.q2.popleft()
            self.isq1 = 1 - self.isq1
        elif self.q1:
            res = self.q1.popleft()
        elif self.q2:
            res = self.q2.popleft()
        return res

    """
    @return: True if has next
    """

    def hasNext(self):
        # write your code here
        return self.q1 or self.q2

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result

v1 = [1, 2]
v2 = [3, 4, 5, 6]
solution, result = ZigzagIterator(v1, v2), []
while solution.hasNext():
    result.append(solution.next())
print(result)
