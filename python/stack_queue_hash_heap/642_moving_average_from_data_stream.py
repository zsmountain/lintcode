'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
'''

from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.q = deque()
        self.sum = 0
    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        # write your code here

        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param = obj.next(val)
        self.q.append(val)
        if len(self.q) > self.size:
            left = self.q.popleft()
            self.sum = self.sum - left + val
        else:
            self.sum += val
        return self.sum / len(self.q)

m = MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.next(5))
